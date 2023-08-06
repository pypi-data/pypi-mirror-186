from typing import Optional, Tuple

import torch.nn as nn

from _finetuner.tailor import to_embedding_model
from _finetuner.tailor.projection import ProjectionHead


def convert_backbone_to_embedding_model(
    backbone: nn.Module,
    embedding_layer: Optional[str] = None,
    embedding_dim: Optional[int] = None,
    output_dim: Optional[int] = None,
    freeze: bool = False,
    tailor_input_shape: Optional[Tuple[int, ...]] = None,
    tailor_input_dtype: str = 'float32',
) -> nn.Module:
    """Convert backbone to embedding model.

    :param backbone: The backbone loaded from the model builders.
    :param embedding_layer: The layer to be used to extract features.
    :param embedding_dim: The dimensionality of the embedding layer.
    :param output_dim: The expected output dimensionality. If set and not equal
        to `embedding_dim`, will attach mlp to the end.
    :param freeze: If freeze the model or not.
    :param tailor_input_shape: The input shape of the model, used to interpret
        the model structure by construct a random tensor and bypass the model.
    :param tailor_input_dtype: The input dtype of the tensor.
    """
    projection_head = None
    embedding_layer = embedding_layer
    embedding_dim = embedding_dim
    output_dim = output_dim

    if freeze and not output_dim:
        output_dim = embedding_dim

    if output_dim and (embedding_dim != output_dim or freeze):
        projection_head = ProjectionHead(
            in_features=embedding_dim, output_dim=output_dim
        )

    model = to_embedding_model(
        model=backbone,
        layer_name=embedding_layer,
        freeze=freeze,
        projection_head=projection_head,
        input_shape=tailor_input_shape,
        input_dtype=tailor_input_dtype,
    )
    return model
