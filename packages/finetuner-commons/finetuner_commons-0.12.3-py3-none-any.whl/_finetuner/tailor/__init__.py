from typing import List, Optional, Tuple, Union

from torch import nn

from _finetuner.tailor.projection import ProjectionHead  # noqa: F401
from _finetuner.tailor.tailor import Tailor  # noqa: F401


def to_embedding_model(
    model: nn.Module,
    layer_name: Optional[str] = None,
    input_shape: Optional[Tuple[int, ...]] = None,
    input_dtype: str = 'float32',
    freeze: Union[bool, List[str]] = False,
    projection_head: Optional[nn.Module] = None,
) -> nn.Module:
    """Convert a general model from :py:attr:`.model` to an embedding model.

    :param model: The DNN model to be converted.
    :param layer_name: The name of the layer that is used for output embeddings. All
        layers *after* that layer will be removed. When set to ``None``, then the last
        layer listed in :py:attr:`.embedding_layers` will be used. To see all available
        names you can check ``name`` field of :py:attr:`.embedding_layers`.
    :param input_shape: The input shape of the DNN model.
    :param input_dtype: The input data type of the DNN model.
    :param freeze: If set as True, will freeze all layers before
        :py:`attr`:`layer_name`. If set as list of str, will freeze layers by names.
    :param projection_head: Attach a module at the end of model, this module should be
        always trainable.
    """
    return Tailor(model, input_shape, input_dtype).to_embedding_model(
        layer_name=layer_name,
        projection_head=projection_head,
        freeze=freeze,
    )


def display(
    model: nn.Module,
    input_shape: Optional[Tuple[int, ...]] = None,
    input_dtype: str = 'float32',
) -> None:
    """Display the model architecture from :py:attr:`.summary` in a table.

    :param model: The DNN model to display.
    :param input_shape: The input shape of the DNN model.
    :param input_dtype: The input data type of the DNN model.
    """
    Tailor(model, input_shape, input_dtype).display()
