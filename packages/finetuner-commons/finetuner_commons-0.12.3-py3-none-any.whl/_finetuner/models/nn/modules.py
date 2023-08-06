from typing import List, Optional

import torch
import torch.nn.functional as f
from torch import nn
from transformers.modeling_outputs import BaseModelOutput

from _finetuner.models.nn.pointnet import PointNet2, PointNetMLP


class CLIP(nn.Module):
    """
    Wraps either a text or an image clip encoder from a hugging face
    transformers.CLIPModel.

    :param clip_encoder: either transformers.CLIPModel.vision_model or
        transformers.CLIPModel.text_model.
    :param clip_projection: either transformers.CLIPModel.visual_projection or
        transformers.CLIPModel.text_projection.
    """

    def __init__(self, clip_encoder: nn.Module, clip_projection: nn.Linear):
        super().__init__()
        self._model = clip_encoder
        self._projection = clip_projection

    def forward(self, *args, **kwargs):
        out = self._model(*args, **kwargs)
        return self._projection(out.pooler_output)


class OpenCLIPVisionModel(nn.Module):
    """
    Wraps the vision encoding model of an Open CLIP model.

    :param clip_model: A pre-trained Open CLIP model loaded with the
        `finetuner.runner.models.builders.load_open_clip_model` function
    """

    def __init__(self, clip_model: nn.Module):
        super().__init__()
        self._model = clip_model

    def forward(self, *args, **kwargs):
        return f.normalize(self._model.encode_image(*args, **kwargs), dim=-1)


class OpenCLIPTextModel(nn.Module):
    """
    Wraps the text encoding model of an Open CLIP model.

    :param clip_model: A pre-trained Open CLIP model loaded with the
        `finetuner.runner.models.builders.load_open_clip_model` function
    """

    def __init__(self, clip_model: nn.Module):
        super().__init__()
        self._model = clip_model

    def forward(self, *args, **kwargs):
        return f.normalize(self._model.encode_text(*args, **kwargs), dim=-1)


class TextTransformer(nn.Module):
    """
    Wraps a text encoder from hugging face transformers, adds a pooling layer.
    The pooler attribute of the provided model is set to None as the forward pass
    is done without making use of the pooling layer of the model.

    :param model: A transformer model from hugging face.
    :param pooling: A `str` to configure the pooling layer: mean/max/cls.
    """

    def __init__(self, model: nn.Module, pooling: str = 'mean'):
        super().__init__()
        self._model = model
        self._model.pooler = None
        self._pooling = pooling

    def _transformer_pooling(
        self,
        model_output: BaseModelOutput,
        attention_mask: torch.Tensor,
    ) -> torch.Tensor:
        """
        Performs pooling on the token embeddings from a transformer model.

        Pooling generates a fixed size sentence embedding from sentences of variable
        length. It also allows the use of the CLS token which the SBert model returns.

        :param model_output: Output from transformer model of type `BaseModelOutput`.
        :param attention_mask: Attention mask `tensor` of shape `[m, n]`
            where `m` is the `batch_size` and `n` is the number of tokens.
        """
        token_embeddings = model_output[0]

        # Pooling strategy
        if self._pooling == 'cls':
            # Take first token by default
            return model_output.get('cls_token_embeddings', token_embeddings[:, 0])

        elif self._pooling == 'max':
            input_mask_expanded = (
                attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
            )
            token_embeddings[input_mask_expanded == 0] = -1e9
            return torch.max(token_embeddings, 1)[0]
        else:
            input_mask_expanded = (
                attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
            )
            sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)

            # If tokens are weighted (by WordWeights layer)
            # feature 'token_weights_sum' will be present
            if 'token_weights_sum' in model_output:
                sum_mask = (
                    model_output['token_weights_sum']
                    .unsqueeze(-1)
                    .expand(sum_embeddings.size())
                )
            else:
                sum_mask = input_mask_expanded.sum(1)

            sum_mask = torch.clamp(sum_mask, min=1e-9)
            return sum_embeddings / sum_mask

    def forward(self, *args, **kwargs):
        out = self._model(*args, **kwargs)
        attention_mask = (
            kwargs['attention_mask'] if 'attention_mask' in kwargs else args[-1]
        )
        return self._transformer_pooling(out, attention_mask)


class MLP(nn.Module):
    """Wrapper for MLP model class.

    :param input_size: Size of the input representations.
    :param hidden_sizes: A list of sizes of the hidden layers. The last hidden size is
        the output size.
    :param bias: Whether to add bias to each layer.
    :param activation: A string to configure activation function, `relu`, `tanh` or
        `sigmoid`. Set to `None` for no activation.
    :param l2: Apply L2 normalization at the output layer.
    """

    def __init__(
        self,
        input_size: int,
        hidden_sizes: List[int],
        bias: bool = True,
        activation: Optional[str] = None,
        l2: bool = False,
    ):
        super().__init__()
        self._l2 = l2
        self._hidden = nn.Sequential()
        self._activation = activation

        if not hidden_sizes:
            hidden_sizes = [input_size]

        for k in range(len(hidden_sizes)):
            self._hidden.append(nn.Linear(input_size, hidden_sizes[k], bias=bias))
            input_size = hidden_sizes[k]
            if activation:
                self._hidden.append(self._get_activation(activation))

    @staticmethod
    def _get_activation(activation: str) -> torch.nn.Module:
        if activation == 'relu':
            return nn.ReLU()
        elif activation == 'tanh':
            return nn.Tanh()
        elif activation == 'sigmoid':
            return nn.Sigmoid()
        else:
            raise ValueError(f'The activation function {activation} is not supported.')

    def forward(self, _input: torch.Tensor):
        proj = self._hidden(_input)
        if self._l2:
            return f.normalize(proj, p=2.0, dim=-1)
        return proj


class MeshDataModel(nn.Module):
    """
    Wraps the PointNet2 model from `_finetuner.models.nn.pointnet`.

    :param hidden_dim: Size of the hidden layers.
    :param embed_dim: Dimensionality of the output embeddings.
    :param input_shape: Defines the semantics of the axes of the input tensors
        (by default: 'bnc', alternative: 'bcn')
    :param dropout_rate: Determines the dropout rates for the dropout layers.
    """

    def __init__(
        self,
        hidden_dim: int = 1024,
        embed_dim: int = 512,
        input_shape: str = 'bnc',
        dropout_rate: float = 0.1,
    ):
        super().__init__()
        self._point_encoder = PointNet2(
            emb_dims=hidden_dim,
            normal_channel=False,
            input_shape=input_shape,
            density_adaptive_type='ssg',
        )

        self._dropout = nn.Dropout(dropout_rate)

        # Projector
        self._projector = PointNetMLP(hidden_dim, hidden_dim * 4, embed_dim)

    def forward(self, points):
        features = self._point_encoder(points)
        features = self._dropout(features)
        return self._projector(features)
