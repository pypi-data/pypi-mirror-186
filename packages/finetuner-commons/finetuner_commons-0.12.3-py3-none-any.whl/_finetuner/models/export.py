import io
from typing import IO, Dict, List, Optional, Tuple, Union

import numpy as np
import onnx
import onnxruntime as ort
import torch
from torch.onnx import TrainingMode


def _check_onnx_graph(f: Union[str, IO[bytes]]) -> None:
    """
    Check an ONNX graph, using the ONNX checker.
    """
    if isinstance(f, str):
        onnx.checker.check_model(f)
    else:
        onnx.checker.check_model(onnx.load(f))


def _random_int_tensor(
    shape: Tuple[int, ...],
    dtype: torch.dtype = torch.int32,
    low: int = 0,
    high: int = 1e5,
) -> torch.Tensor:
    """
    Randomly generate an int Tensor.
    """
    return torch.randint(
        low=low, high=high, size=shape, requires_grad=False, dtype=dtype
    )


def _random_float_tensor(
    shape: Tuple[int, ...],
    dtype: torch.dtype = torch.float32,
) -> torch.Tensor:
    """
    Randomly generate a float Tensor.
    """
    return torch.randn(shape, requires_grad=False, dtype=dtype)


def _random_tensor(
    shape: Tuple[int, ...],
    dtype: torch.dtype = torch.int32,
    int_low: int = 0,
    int_high: int = 1e5,
) -> torch.Tensor:
    """
    Randomly generate a float or int Tensor.
    """
    if 'int' in str(dtype):
        return _random_int_tensor(shape, dtype, int_low, int_high)
    return _random_float_tensor(shape, dtype)


def _validate_onnx_output(
    model: torch.nn.Module,
    f: Union[str, IO[bytes]],
    inputs: Tuple[torch.Tensor, ...],
) -> None:
    """
    Test an exported model by comparing the outputs of the original and the exported
    model against the same input.
    """

    inputs_np = [inp.cpu().numpy() for inp in inputs]
    providers = ['CPUExecutionProvider']

    session = (
        ort.InferenceSession(f, providers=providers)
        if isinstance(f, str)
        else ort.InferenceSession(f.read(), providers=providers)
    )
    y_exported = session.run(
        None, {session.get_inputs()[i].name: x for i, x in enumerate(inputs_np)}
    )
    with torch.no_grad():
        y_original = model(*inputs)

    if isinstance(y_original, torch.Tensor):
        y_original = [y_original]
    elif isinstance(y_original, dict):
        y_original = [tensor for _, tensor in y_original.items()]

    y_original = [y.detach().cpu().numpy() for y in y_original]

    for yo, ye in zip(y_original, y_exported):
        np.testing.assert_allclose(yo, ye, rtol=1e-03, atol=1e-03)


def to_onnx_format(
    model: torch.nn.Module,
    f: Union[str, IO[bytes]],
    input_shapes: List[Tuple[int, ...]],
    input_dtypes: List[torch.dtype],
    input_names: Optional[List[str]] = None,
    output_names: Optional[List[str]] = None,
    dynamic_axes: Optional[Dict[str, Dict[int, str]]] = None,
    opset_version: int = 16,
    random_int_low: Optional[List[Union[None, int]]] = None,
    random_int_high: Optional[List[Union[None, int]]] = None,
    max_int: int = 10000,
) -> None:
    """
    Convert a PyTorch model to an ONNX graph.

    :param model: Input PyTorch model.
    :param f: Export file, either a path or a byte stream.
    :param input_names: A list of unique input names. Each name should correspond to an
        input in your model.
    :param output_names: A list of unique output names. Each name should correspond to
        an output of your model.
    :param input_shapes: A list of input shapes. Each element in the list should be the
        shape of the respective input defined in ``input_names``.
    :param input_dtypes: A list of torch dtypes. Each element in the list should be the
        dtype of the respective input defined in ``input_names``.
    :param dynamic_axes: Dynamic axes to pass to the ONNX exporter. Usually batch size
        and sequence length are defined as dynamic axes. If set to None, no dynamic
        axes are specified.
    :param opset_version: The ONNX parameter set to use. Defaults to the latest.
    :param random_int_low: Most text models accept inputs of type int. In order to
        construct a random input for tracing, a random int tensor needs to be created.
        This argument specifies the min value in this tensor. Usually it should be set
        to 0. Has no effect if your model input types are float.
    :param random_int_high: Similar to the `random_int_low` argument, this specifies
        the max value in the random int tensor. This should be usually set to your
        model's vocab size. Has no effect if your model input types are float.
    :param max_int: In case `random_int_high` is not specified, we'll it with a list of
        `max_int`s.
    """
    _original_device = next(model.parameters()).device
    model.to('cpu')

    _is_training_before = model.training
    model.eval()

    if not input_names:
        input_names = [f'input-{i}' for i in range(len(input_shapes))]

    if not output_names:
        output_names = ['output']

    assert len(input_names) == len(set(input_names))
    assert len(output_names) == len(set(output_names))

    if not random_int_low:
        random_int_low = [0 for _ in range(len(input_shapes))]

    if not random_int_high:
        random_int_high = [max_int for _ in range(len(input_shapes))]

    assert (
        len(input_names)
        == len(input_shapes)
        == len(input_dtypes)
        == len(random_int_low)
        == len(random_int_high)
    )

    # export to ONNX
    inputs = ()
    for shape, dtype, int_low, int_high in zip(
        input_shapes, input_dtypes, random_int_low, random_int_high
    ):
        inputs += (_random_tensor(shape, dtype, int_low, int_high),)

    with torch.no_grad():
        torch.onnx.export(
            model,
            inputs,
            f,
            opset_version=opset_version,
            input_names=input_names,
            output_names=output_names,
            dynamic_axes=dynamic_axes,
            do_constant_folding=True,
            training=TrainingMode.EVAL,
            verbose=False,
        )

    if isinstance(f, io.BytesIO):
        f.seek(0)
    _check_onnx_graph(f)

    inputs = ()
    for shape, dtype, int_low, int_high in zip(
        input_shapes, input_dtypes, random_int_low, random_int_high
    ):
        inputs += (_random_tensor(shape, dtype, int_low, int_high),)

    if isinstance(f, io.BytesIO):
        f.seek(0)

    if isinstance(f, io.BytesIO):
        f.seek(0)
    _validate_onnx_output(model, f, inputs)

    if _is_training_before:
        model.train()

    model.to(_original_device)


def to_torch_format(
    model: torch.nn.Module,
    f: Union[str, IO[bytes]],
):
    """Save the embedding model.

    :param model: The tuned model to save as torch format.
    :param f: Export file, either a path or a byte stream.
    """
    _original_device = next(model.parameters()).device
    model.to('cpu')

    _is_training_before = model.training
    model.eval()

    torch.save(model.state_dict(), f)

    if _is_training_before:
        model.train()

    model.to(_original_device)
