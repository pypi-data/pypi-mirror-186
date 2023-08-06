import abc
from typing import Optional, TypeVar

from torch import nn
from transformers import AutoModel

from _finetuner.models.nn.modules import (
    CLIP,
    MLP,
    MeshDataModel,
    OpenCLIPTextModel,
    OpenCLIPVisionModel,
    TextTransformer,
)

BackboneBuilderType = TypeVar('BackboneBuilderType', bound='_BackboneBuilder')


def load_open_clip_model(descriptor: str) -> nn.Module:
    """
    Loads a pre-trained Open CLIP model from a given descriptor.

    :param descriptor: Refers to a pre-trained open clip model.
    :return: An Open CLIP PyTorch model.
    """
    import open_clip

    name, pretrained = descriptor.split('::')
    return open_clip.create_model(name, pretrained=pretrained)


class _BackboneBuilder(metaclass=abc.ABCMeta):
    """Base backbone model builder."""

    _supports_tailor: bool = False

    def __init__(self, descriptor: str, options: Optional[dict] = None) -> None:
        self._descriptor = descriptor
        self._options = options

    def __call__(self) -> nn.Module:
        return self.build()

    @abc.abstractmethod
    def build(self) -> nn.Module:
        ...


class CNNBuilder(_BackboneBuilder):
    """Build a CNN based model using the torchvision library."""

    _supports_tailor = True

    def build(self) -> nn.Module:
        import torchvision

        return getattr(torchvision.models, self._descriptor)(pretrained=True)


class CLIPTextBuilder(_BackboneBuilder):
    """Build a CLIP text model using the transformers package."""

    def build(self) -> nn.Module:
        model = AutoModel.from_pretrained(self._descriptor)
        return CLIP(model.text_model, model.text_projection)


class CLIPVisionBuilder(_BackboneBuilder):
    """Build a CLIP vision model using the transformers package."""

    def build(self) -> nn.Module:
        model = AutoModel.from_pretrained(self._descriptor)
        return CLIP(model.vision_model, model.visual_projection)


class OpenCLIPTextBuilder(_BackboneBuilder):
    """Build a text transformer model for an Open CLIP model."""

    def build(self) -> nn.Module:
        model = load_open_clip_model(self._descriptor)
        return OpenCLIPTextModel(model)


class OpenCLIPVisionBuilder(_BackboneBuilder):
    """Build a vision model for an Open CLIP model."""

    def build(self) -> nn.Module:
        model = load_open_clip_model(self._descriptor)
        return OpenCLIPVisionModel(model)


class TextTransformerBuilder(_BackboneBuilder):
    """Build a text transformer model using huggingface transformers."""

    def build(self) -> nn.Module:
        model = AutoModel.from_pretrained(self._descriptor)
        return TextTransformer(model, **self._options)


class MLPBuilder(_BackboneBuilder):
    """Build an MLP model from scratch, to fine-tune with pre-embedded documents."""

    def build(self) -> nn.Module:
        return MLP(**self._options)


class MeshDataModelBuilder(_BackboneBuilder):
    """Builds a model for encding meshes"""

    def build(self) -> nn.Module:
        return MeshDataModel(**self._options)
