import abc
import io
import logging
import multiprocessing as mp
import os
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union

import numpy as np
import onnxruntime as ort
import torch
from docarray import DocumentArray

from _finetuner.data import collate, preprocess, utils
from _finetuner.excepts import (
    CorruptedMetadata,
    CorruptedONNXModel,
    SelectModelRequired,
)
from _finetuner.models import builders
from _finetuner.models.load import load_artifact
from _finetuner.models.utils import convert_backbone_to_embedding_model
from _finetuner.runner.artifact import RunArtifact
from _finetuner.runner.model import RunnerModel

logger = logging.getLogger(__name__)


class InferenceEngine(abc.ABC):
    _artifact: Union[str, RunnerModel]
    _is_onnx: bool
    _token: Optional[str]
    _batch_size: int
    _select_model: str
    _device: str
    _device_id: int
    _logging_level: str
    _model_name: str
    _metadata: Dict[str, Any]
    _model_dump: Union[None, str, io.BytesIO]
    _input_names: List[str]
    _input_shapes: List[Tuple[Union[str, int]]]
    _output_name: str
    _output_shape: Tuple[Union[int, str]]
    _multi_modal: bool
    _data_handler: utils.PreprocessCollateWrapper
    _builder: str
    _options: dict
    _descriptor: str
    _embedding_layer: Optional[str]
    _output_dim: Optional[int]
    _freeze: bool
    _tailor_input_shape: Tuple[int, ...]
    _tailor_input_dtype: str

    def __init__(
        self,
        artifact: Union[str, RunnerModel, RunArtifact],
        is_onnx: bool = False,
        token: Optional[str] = None,
        batch_size: int = 32,
        select_model: Optional[str] = None,
        device: str = 'cpu',
        device_id: int = 0,
        logging_level: str = 'DEBUG',
        **kwargs,
    ) -> None:
        """
        The finetuner inference engine can load any model trained with Finetuner and
        use it to encode Documents. Alternatively, a pre-trained model in the compatible
        finetuner format can be provided instead of a finetuned one.

        :param artifact: Specify a finetuner run artifact. Can be a path to a local
            directory, a path to a local zip file or a Hubble artifact ID. Individual
            model artifacts (model subfolders inside the run artifacts) can also be
            specified using this argument. An in-memory object, either a
            :class:`RunnerModel` or a :class:`RunArtifact`, can be passed as well.
        :param is_onnx: If the model is an onnx model or not. If you call the
            :meth:`fit` function with `to_onnx=True`, please set this parameter as
            `True`.
        :param token: A Jina authentication token required for pulling artifacts from
            Hubble. If not provided, the Hubble client will try to find one either in a
            local cache folder or in the environment.
        :param batch_size: Incoming documents are fed to the graph in batches, both to
            speed-up inference and avoid memory errors. This argument controls the
            number of documents that will be put in each batch.
        :param select_model: Finetuner run artifacts might contain multiple models. In
            such cases you can select which model to deploy using this argument.
        :param device: The device to use for inference. Either `cpu` or `cuda`.
        :param device_id: Specify which CPU or GPU to use for inference.
        :param logging_level: The executor logging level. See
            https://docs.python.org/3/library/logging.html#logging-levels for available
            options.
        """
        self._is_onnx = is_onnx
        self._token = token
        self._batch_size = batch_size
        self._select_model = select_model
        self._device = device.lower().strip()
        self._device_id = device_id
        self._torch_device = torch.device(self._device)
        self._logging_level = logging_level

        # noinspection PyUnresolvedReferences
        assert self._logging_level in logging._nameToLevel
        logger.setLevel(self._logging_level)

        logger.info('Starting the inference engine ...')
        logger.debug(f'Device set to [{self._device}]')
        logger.debug(f'Device ID set to [{self._device_id}]')
        logger.debug(f'Batch size set to [{self._batch_size}]')
        self._artifact = self._load_artifact(artifact)
        self._check_metadata()
        self._build_data_pipeline()

    def _load_artifact(
        self,
        artifact: Union[str, RunnerModel, RunArtifact],
    ) -> Union[str, RunnerModel]:
        """
        If artifact is a string, then load the artifact either from a directory,
        a zip file or directly from Hubble.
        If artifact is a :class:`RunnerModel` or :class:`RunArtifact`, then load the
        artifact directly from memory.

        :param artifact: The artifact passed at construction
        :return: The artifact to be used by the engine going forward. In the case that a
            :class:`RunArtifact` is passed, then a :class:`RunnerModel` will be
            returned, otherwise the input artifact will be returned
        """

        logger.info('Loading artifact ...')

        if isinstance(artifact, str):
            logger.debug(f'Artifact as path set to [{artifact}]')
            self._model_name, self._metadata, self._model_dump = load_artifact(
                artifact=artifact,
                is_onnx=self._is_onnx,
                select_model=self._select_model,
                token=self._token,
            )

        elif isinstance(artifact, RunArtifact):
            models = artifact.models
            if len(models) > 1:
                if self._select_model:
                    artifact = models[self._select_model]
                else:
                    raise SelectModelRequired(
                        'Found more than 1 model recorded in RunArtifact, '
                        'please select model using `select_model`'
                    )
            else:
                artifact = models[list(models.keys())[0]]

        if isinstance(artifact, RunnerModel):
            logger.debug(f'Artifact as RunnerModel set to [{artifact._stub.name}]')
            self._model_name = artifact._stub.name
            self._metadata = artifact.metadata
            if self._is_onnx:
                self._model_dump = io.BytesIO()
                artifact.export(
                    model=artifact.build(),
                    f=self._model_dump,
                    to_onnx=self._is_onnx,
                )
        elif not isinstance(artifact, str):
            raise TypeError(f'{type(artifact)} is not a valid type for artifact')

        return artifact

    def _check_metadata(self):
        """Check the model metadata."""
        logger.info('Checking the model metadata ...')

        try:
            self._builder = self._metadata['builder']
            self._options = self._metadata['options']
            self._descriptor = self._metadata['descriptor']
            self._input_names = self._metadata['input_names']
            self._input_shapes = self._metadata['input_shapes']
            self._output_name = self._metadata['output_name']
            self._output_shape = self._metadata['output_shape']
            self._embedding_layer = self._metadata['embedding_layer']
            self._output_dim = self._metadata['output_dim']
            self._freeze = self._metadata['freeze']
            self._tailor_input_shape = self._metadata['tailor_input_shape']
            self._tailor_input_dtype = self._metadata['tailor_input_dtype']
        except KeyError as exc:
            raise CorruptedMetadata(f'Key is missing, details: {str(exc)}')

        if len(self._input_names) != len(self._input_shapes):
            raise CorruptedMetadata(
                'Length mismatch between keys \'input_names\' and \'input_shapes\''
            )

        for name, shape in zip(self._input_names, self._input_shapes):
            logger.debug(f'Input {name}: {shape}')

        logger.debug(f'Output: {self._output_shape}')

        _input_dynamic_axes = {
            dim
            for _input_shape in self._input_shapes
            for dim in _input_shape
            if isinstance(dim, str)
        }
        _output_dynamic_axes = {
            dim for dim in self._output_shape if isinstance(dim, str)
        }
        _set_difference = _output_dynamic_axes - _input_dynamic_axes
        if len(_set_difference) > 0:
            raise CorruptedMetadata(
                f'Output dynamic axes {_set_difference} not found in the inputs. '
                'Dynamic shape inference will fail'
            )

    def _build_data_pipeline(self):
        """Configure the preprocess and the collate functions from the model
        metadata.
        """
        logger.info('Building the data pipeline ...')

        preprocess_fns = {}
        collate_fns = {}

        try:
            modalities = list(self._metadata['preprocess_types'].keys())
            logger.debug(f'Modalities: {modalities}')

            for modality in modalities:
                preprocess_type = self._metadata['preprocess_types'][modality]
                preprocess_options = self._metadata['preprocess_options'][modality]
                collate_type = self._metadata['collate_types'][modality]
                collate_options = self._metadata['collate_options'][modality]

                preprocess_fn = getattr(preprocess, preprocess_type)(
                    **preprocess_options
                )

                collate_fn = getattr(collate, collate_type)(**collate_options)

                logger.debug(
                    f'{modality} - {preprocess_type}({preprocess_options}) '
                    f'{preprocess_type}({preprocess_options})'
                )

                preprocess_fns[modality] = preprocess_fn
                collate_fns[modality] = collate_fn

        except Exception as exc:
            raise CorruptedMetadata(
                f'Preprocess and collate are misconfigured, details: {str(exc)}'
            )

        self._multi_modal = len(modalities) > 1
        self._data_handler = utils.PreprocessCollateWrapper(
            preprocess_fns, collate_fns, self._multi_modal
        )

    def _run_data_pipeline(
        self,
        docs: DocumentArray,
    ) -> Dict[str, Union[torch.Tensor, Mapping]]:
        """Run documents through the data pipeline."""
        return self._data_handler.collate_contents(
            [self._data_handler.preprocess(doc) for doc in docs]
        )

    @staticmethod
    def _flatten_inputs(
        inputs: Dict[str, Union[torch.Tensor, Mapping]],
    ) -> Dict[str, torch.Tensor]:
        """Run documents through the data pipeline."""
        tensors = {}
        for _input_name, _input in inputs.items():
            if isinstance(_input, torch.Tensor):
                tensors[_input_name] = _input
            elif isinstance(_input, Mapping):
                for _sub_input_name, _sub_input in _input.items():
                    if not isinstance(_sub_input, torch.Tensor):
                        raise RuntimeError(
                            f'Got unexpected type {type(_sub_input)} for input '
                            f'name {_sub_input_name}'
                        )
                    tensors[_sub_input_name] = _sub_input
            else:
                raise RuntimeError(
                    f'Got unexpected type {type(_input)} for input name '
                    f'{_input_name}'
                )
        return tensors

    def _check_input_names(self, inputs: Dict[str, torch.Tensor]) -> None:
        """Run documents through the data pipeline."""
        _set_given_inputs = set(inputs.keys())
        _set_expected_inputs = set(self._input_names)
        if _set_given_inputs.intersection(_set_expected_inputs) != _set_expected_inputs:
            raise RuntimeError(
                f'Expected input names {self._input_names}, got {list(inputs.keys())}'
            )

    def _move_to_device(
        self, inputs: Dict[str, torch.Tensor]
    ) -> Dict[str, torch.Tensor]:
        """Moves tensor to device."""
        tensors = {}
        for _input_name, _input_tensor in inputs.items():
            if _input_tensor.dtype in [torch.int64, torch.long]:
                # int32 mandatory as input of bindings, int64 not supported
                tensors[_input_name] = _input_tensor.int().to(self._torch_device)
            else:
                tensors[_input_name] = _input_tensor.to(self._torch_device)
        return tensors

    @property
    def _numpy_to_torch_dtype(self):
        # https://github.com/pytorch/pytorch/blob/ac79c874cefee2f8bc1605eed9a924d80c0b3542/torch/testing/_internal/common_utils.py#L349
        return {
            bool: torch.bool,
            np.uint8: torch.uint8,
            np.int8: torch.int8,
            np.int16: torch.int16,
            np.int32: torch.int32,
            np.int64: torch.int64,
            np.float16: torch.float16,
            np.float32: torch.float32,
            np.float64: torch.float64,
            np.complex64: torch.complex64,
            np.complex128: torch.complex128,
        }

    @property
    def _torch_to_numpy_dtype(self):
        return {v: k for k, v in self._numpy_to_torch_dtype.items()}

    @abc.abstractmethod
    def run(
        self,
        inputs: Dict[str, torch.Tensor],
        output_shape: Tuple[int, ...],
    ) -> torch.Tensor:
        """Run inference pipeline.

        :param inputs: flattened inputs represented as input names and tensor.
        :param output_shape: additional arguments.
        """
        ...


class TorchInferenceEngine(InferenceEngine):
    def __init__(
        self,
        artifact: Union[str, RunnerModel, RunArtifact],
        is_onnx: bool = False,
        token: Optional[str] = None,
        batch_size: int = 32,
        select_model: Optional[str] = None,
        device: str = 'cpu',
        device_id: int = 0,
        logging_level: str = 'DEBUG',
        **kwargs,
    ) -> None:
        """
        The finetuner inference engine can load any model trained with Finetuner and use
        it to encode Documents. Alternatively, a pre-trained model in the compatible
        finetuner format can be provided instead of a finetuned one.

        :param artifact: Specify a finetuner run artifact. Can be a path to a local
            directory, a path to a local zip file or a Hubble artifact ID. Individual
            model artifacts (model subfolders inside the run artifacts) can also be
            specified using this argument. An in-memory object, either a
            :class:`RunnerModel` or a :class:`RunArtifact`, can be passed as well.
        :param is_onnx: If the model is an onnx model or not. If you call the
            :meth:`fit` function with `to_onnx=True`, please set this parameter as
            `True`.
        :param token: A Jina authentication token required for pulling artifacts from
            Hubble. If not provided, the Hubble client will try to find one either in a
            local cache folder or in the environment.
        :param batch_size: Incoming documents are fed to the graph in batches, both to
            speed-up inference and avoid memory errors. This argument controls the
            number of documents that will be put in each batch.
        :param select_model: Finetuner run artifacts might contain multiple models. In
            such cases you can select which model to deploy using this argument.
        :param device: The device to use for inference. Either `cpu` or `cuda`.
        :param device_id: Specify which CPU or GPU to use for inference.
        :param logging_level: The executor logging level. See
            https://docs.python.org/3/library/logging.html#logging-levels for available
            options.
        """
        super().__init__(
            artifact=artifact,
            is_onnx=is_onnx,
            token=token,
            batch_size=batch_size,
            select_model=select_model,
            device=device,
            device_id=device_id,
            logging_level=logging_level,
            **kwargs,
        )
        self._model = self._build_torch_model()

    def _build_torch_model(self):
        if isinstance(self._artifact, RunnerModel):
            model = self._artifact.build()
        elif isinstance(self._artifact, str):
            builder_cls = getattr(builders, self._builder)
            builder = builder_cls(self._descriptor, self._options)
            model = builder()
            if builder._supports_tailor:
                model = convert_backbone_to_embedding_model(
                    backbone=model,
                    embedding_layer=self._embedding_layer,
                    embedding_dim=self._output_shape[-1],
                    output_dim=self._output_dim,
                    freeze=self._freeze,
                    tailor_input_shape=tuple(self._tailor_input_shape),
                    tailor_input_dtype=self._tailor_input_dtype,
                )
            model.load_state_dict(torch.load(self._model_dump))
            self._model_dump = None
        else:
            raise TypeError(f'{type(self._artifact)} is not a valid type for artifact')

        model.to(self._torch_device)
        model.eval()
        return model

    def run(
        self,
        inputs: Dict[str, torch.Tensor],
        *_,
        **__,
    ) -> torch.Tensor:
        """Run inference pipeline.

        :param inputs: flattened inputs represented as input names and tensor.
        """
        if len(self._input_names) == 1:
            tensor = inputs[self._input_names[0]].contiguous()
            outputs = self._model(tensor)
        else:
            outputs = self._model(**inputs)
        return outputs


class ONNXRuntimeInferenceEngine(InferenceEngine):
    _omp_num_threads: int
    _intra_op_num_threads: int
    _inter_op_num_threads: int

    # noinspection PyUnresolvedReferences
    _session_options: ort.SessionOptions
    _providers: List[str]
    _session: ort.InferenceSession

    def __init__(
        self,
        artifact: Union[str, RunnerModel, RunArtifact],
        is_onnx: bool = True,
        token: Optional[str] = None,
        batch_size: int = 32,
        select_model: Optional[str] = None,
        device: str = 'cpu',
        device_id: int = 0,
        omp_num_threads: int = mp.cpu_count(),
        intra_op_num_threads: int = 0,
        inter_op_num_threads: int = 0,
        logging_level: str = 'DEBUG',
        **kwargs,
    ) -> None:
        """
        The finetuner inferencer can load any model trained with Finetuner and use it to
        encode Documents. Alternatively, a pre-trained model in the compatible finetuner format
        can be provided instead of a finetuned one.

        :param artifact: Specify a finetuner run artifact. Can be a path to a local
            directory, a path to a local zip file or a Hubble artifact ID. Individual
            model artifacts (model subfolders inside the run artifacts) can also be
            specified using this argument. An in-memory object, either a
            :class:`RunnerModel` or a :class:`RunArtifact`, can be passed as well.
        :param is_onnx: If the model is an onnx model or not. If you call the
            :meth:`fit` function with `to_onnx=True`, please set this parameter as `True`.
        :param token: A Jina authentication token required for pulling artifacts from
            Hubble. If not provided, the Hubble client will try to find one either in a
            local cache folder or in the environment.
        :param batch_size: Incoming documents are fed to the graph in batches, both to
            speed-up inference and avoid memory errors. This argument controls the
            number of documents that will be put in each batch.
        :param select_model: Finetuner run artifacts might contain multiple models. In
            such cases you can select which model to deploy using this argument.
        :param device: The device to use for inference. Either `cpu` or `cuda`.
        :param device_id: Specify which CPU or GPU to use for inference.
        :param omp_num_threads: The number of threads set by OpenMP. Check out
            https://www.openmp.org/spec-html/5.0/openmpse50.html for more information.
            By default, it is set to the number of available CPUs.
        :param intra_op_num_threads: The execution of an individual operation (for some
            operation types) can be parallelized on a pool of `intra_op_num_threads`. 0
            means the system picks an appropriate number.
            See https://onnxruntime.ai/docs/api/python/api_summary.html#onnxruntime.SessionOptions.intra_op_num_threads  # noqa: E501
        :param inter_op_num_threads: Nodes that perform blocking operations are enqueued
            on a pool of `inter_op_num_threads` available in each process. 0 means
            the system picks an appropriate number.
            See https://onnxruntime.ai/docs/api/python/api_summary.html#onnxruntime.SessionOptions.inter_op_num_threads  # noqa: E501
        :param logging_level: The executor logging level. See
            https://docs.python.org/3/library/logging.html#logging-levels for available
            options.
        """

        super().__init__(
            artifact=artifact,
            is_onnx=is_onnx,
            token=token,
            batch_size=batch_size,
            select_model=select_model,
            device=device,
            device_id=device_id,
            logging_level=logging_level,
            **kwargs,
        )

        self._omp_num_threads = omp_num_threads
        self._intra_op_num_threads = intra_op_num_threads
        self._inter_op_num_threads = inter_op_num_threads

        logger.debug(f'OpenMP num threads set to [{self._omp_num_threads}]')
        logger.debug(
            f'Intra operation num threads set to [{self._intra_op_num_threads}]'
        )
        logger.debug(
            f'Inter operation num threads set to [{self._inter_op_num_threads}]'
        )

        self._configure_onnx_runtime()
        self._build_onnx_graph()

    """ Start-up methods """

    def _configure_onnx_runtime(self):
        """
        Configure the ONNX Runtime options.
        """
        logger.info('Configuring the ONNX runtime ...')

        if self._device not in ['cpu', 'cuda']:
            raise ValueError(f'Unknown device type \'{self._device}\'')

        # noinspection PyUnresolvedReferences
        self._session_options = ort.SessionOptions()
        self._providers = []

        if self._device == 'cpu':

            os.environ['OMP_NUM_THREADS'] = str(self._omp_num_threads)
            self._providers = ['CPUExecutionProvider']

            # noinspection PyUnresolvedReferences
            self._session_options.execution_mode = (
                ort.ExecutionMode.ORT_SEQUENTIAL
                if self._intra_op_num_threads <= 1
                else ort.ExecutionMode.ORT_PARALLEL
            )
            self._session_options.intra_op_num_threads = self._intra_op_num_threads

            if self._inter_op_num_threads > 1:
                self._session_options.inter_op_num_threads = self._inter_op_num_threads

        else:
            self._providers = ['CUDAExecutionProvider']

    def _build_onnx_graph(self):
        """Load the ONNX model."""
        logger.info('Building the ONNX graph ...')
        try:

            if isinstance(self._model_dump, str):
                f = self._model_dump
            else:
                self._model_dump.seek(0)
                f = self._model_dump.read()
                self._model_dump = None

            self._session = ort.InferenceSession(
                f, self._session_options, providers=self._providers
            )

        except Exception as exc:
            raise CorruptedONNXModel(
                f'ONNX model appears to be corrupted, details: {str(exc)}'
            )

        if len(self._session.get_outputs()) != 1:
            raise CorruptedMetadata(
                'Multi-output models are not supported, '
                f'ONNX graph outputs: {self._session.get_outputs()}'
            )

        onnx_input_names = [node.name for node in self._session.get_inputs()]
        if set(onnx_input_names) != set(self._input_names):
            raise CorruptedMetadata(
                f'Invalid ONNX graph inputs {onnx_input_names}, '
                f'expected {self._input_names}'
            )

    """ Runtime methods """

    def _infer_output_shape(self, inputs: Dict[str, torch.Tensor]) -> Tuple[int, ...]:
        """Infer the output shape by inspecting the input tensors. Every dynamic axis
        in the output shape is replaced by the value of the same axis in the input.
        """
        _dynamic_axes: Dict[str, int] = {}
        for name, shape in zip(self._input_names, self._input_shapes):
            tensor = inputs[name]
            for _given_dim, _expected_dim in zip(tensor.shape, shape):
                if isinstance(_expected_dim, str):
                    _dynamic_axes[_expected_dim] = _given_dim
                else:
                    if _given_dim != _expected_dim:
                        raise RuntimeError(
                            f'Shape mismatch, expected {shape} got {tensor.shape}'
                        )
        return tuple(
            [
                _dynamic_axes[dim] if isinstance(dim, str) else dim
                for dim in self._output_shape
            ]
        )

    def run(
        self,
        inputs: Dict[str, torch.Tensor],
        output_shape: Tuple[int, ...],
    ) -> torch.Tensor:
        """Performs inference on ONNX Runtime in an optimized way. In particular,
        avoids some tensor copies from GPU to host by using Torch tensors
        directly."""

        binding: ort.IOBinding = self._session.io_binding()

        _inputs = {}
        for _input_name in self._input_names:
            tensor = inputs[_input_name].contiguous()
            binding.bind_input(
                name=_input_name,
                device_type=self._device,
                device_id=self._device_id,
                element_type=self._torch_to_numpy_dtype[tensor.dtype],
                shape=tuple(tensor.shape),
                buffer_ptr=tensor.data_ptr(),
            )
            _inputs[_input_name] = tensor

        output = torch.empty(
            output_shape, dtype=torch.float32, device=self._torch_device
        ).contiguous()

        binding.bind_output(
            name=self._output_name,
            device_type=self._device,
            device_id=self._device_id,
            element_type=np.float32,  # hard coded output type
            shape=output_shape,
            buffer_ptr=output.data_ptr(),
        )

        self._session.run_with_iobinding(binding)

        return output
