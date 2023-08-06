import random
from typing import TYPE_CHECKING, Any, BinaryIO, Dict, List, Optional, Tuple, Union

import torch
from torch import nn

from _finetuner.data import collate, preprocess
from _finetuner.models import builders
from _finetuner.models.export import to_onnx_format, to_torch_format
from _finetuner.models.utils import convert_backbone_to_embedding_model
from _finetuner.runner.stubs.model import ModelStubType

if TYPE_CHECKING:
    from finetuner.helper import CollateFnType, PreprocessFnType


class RunnerModel:
    """
    A class that wraps a model builder and a stub in a container ready to be used in
    the runner.
    """

    def __init__(
        self,
        stub: ModelStubType,
        freeze: bool = False,
        output_dim: Optional[int] = None,
    ) -> None:
        self._stub = stub
        self._freeze = freeze
        self._output_dim = output_dim
        self._builder = getattr(builders, self._stub.builder)(
            self._stub.descriptor, self._stub.options
        )

    @staticmethod
    def _random_dynamic_shapes() -> Dict[str, int]:
        """Get random values for the dynamic shapes."""
        return {
            'batch-size': random.choice([8, 16, 32]),
            'sequence-length': random.choice([20, 30, 50]),
        }

    @property
    def embedding_dim(self) -> int:
        return self._stub.output_shape[-1]

    @embedding_dim.setter
    def embedding_dim(self, value: int) -> None:
        self._stub.output_shape = self._stub.output_shape[:-1] + (value,)

    def _random_input_shapes(self) -> List[Tuple[int, ...]]:
        _random_dynamic_shapes = self._random_dynamic_shapes()
        return [
            tuple(
                [
                    _random_dynamic_shapes[dim] if isinstance(dim, str) else dim
                    for dim in shape
                ]
            )
            for shape in self._stub.input_shapes
        ]

    def _tailor_input_shape(self) -> Tuple[int, ...]:
        # TODO: tailor only supports 1 input at the moment
        # TODO: tailor adds batch size automatically
        return self._random_input_shapes()[0][1:]

    def _tailor_input_dtype(self) -> str:
        # TODO: tailor only supports 1 input at the moment
        return self._stub.input_dtypes[0]

    @property
    def _input_dtypes(self) -> List[torch.dtype]:
        return [getattr(torch, dtype) for dtype in self._stub.input_dtypes]

    def build(self):
        """Build model."""
        backbone = self._builder()
        if self._builder._supports_tailor:
            return convert_backbone_to_embedding_model(
                backbone=backbone,
                embedding_layer=self._stub.embedding_layer,
                embedding_dim=self.embedding_dim,
                output_dim=self._output_dim,
                freeze=self._freeze,
                tailor_input_shape=self._tailor_input_shape(),
                tailor_input_dtype=self._tailor_input_dtype(),
            )
        else:
            return backbone

    @property
    def preprocess_fn(self) -> Dict[str, 'PreprocessFnType']:
        return {
            modality: getattr(preprocess, preprocess_type)(
                **self._stub.preprocess_options[modality]
            )
            for modality, preprocess_type in self._stub.preprocess_types.items()
        }

    @property
    def collate_fn(self) -> Dict[str, 'CollateFnType']:
        return {
            modality: getattr(collate, collate_type)(
                **self._stub.collate_options[modality]
            )
            for modality, collate_type in self._stub.collate_types.items()
        }

    def export(self, model: nn.Module, f: Union[str, BinaryIO], to_onnx: bool):
        """Export model to either PyTorch or ONNX format.

        :param model: The pytorch model to export.
        :param f: Export path or `BytesIO` object.
        :param to_onnx: Set to True for ONNX exports.
        """
        if to_onnx:
            to_onnx_format(
                model=model,
                f=f,
                input_shapes=self._random_input_shapes(),
                input_dtypes=self._input_dtypes,
                input_names=self._stub.input_names,
                output_names=[self._stub.output_name],
                dynamic_axes=self._stub.dynamic_axes,
            )
        else:
            to_torch_format(model=model, f=f)

    @property
    def metadata(self) -> Dict[str, Any]:
        """Get the model metadata."""
        return {
            'name': self._stub.name,
            'descriptor': self._stub.descriptor,
            'description': self._stub.description,
            'task': self._stub.task,
            'architecture': self._stub.architecture,
            'builder': self._stub.builder,
            'input_names': self._stub.input_names,
            'input_shapes': self._stub.input_shapes,
            'input_dtypes': self._stub.input_dtypes,
            'output_name': self._stub.output_name,
            'output_shape': self._stub.output_shape,
            'dynamic_axes': self._stub.dynamic_axes,
            'preprocess_types': self._stub.preprocess_types,
            'collate_types': self._stub.collate_types,
            'preprocess_options': self._stub.preprocess_options,
            'collate_options': self._stub.collate_options,
            'options': self._stub.options,
            # tailor related metadata
            'embedding_layer': self._stub.embedding_layer,
            'output_dim': self._output_dim,
            'freeze': self._freeze,
            'tailor_input_shape': self._tailor_input_shape(),
            'tailor_input_dtype': self._tailor_input_dtype(),
        }
