import copy
from collections import OrderedDict
from typing import List, Optional, Sequence, Tuple, Union

import numpy as np
import torch
import torch.nn as nn

from _finetuner.tailor.display import DisplayMixin


def is_seq_int(tp) -> bool:
    """Return True if the input is a sequence of integers."""
    return tp and isinstance(tp, Sequence) and all(isinstance(p, int) for p in tp)


class Tailor(DisplayMixin):
    def __init__(
        self,
        model: nn.Module,
        input_shape: Optional[Tuple[int, ...]] = None,
        input_dtype: str = 'float32',
    ):
        """
        Tailor converts a general DNN model into an embedding model.

        :param model: a general DNN model
        :param input_shape: a sequence of integers defining the shape of the input
            tensor. Note, batch size is *not* part of ``input_shape``. It is required
            for :py:class:`Tailor`.
        :param input_dtype: the data type of the input tensor.
        """
        self._model = model

        # multiple inputs to the network
        if isinstance(input_shape, tuple):
            input_shape = [input_shape]

        self._input_shape = input_shape
        self._input_dtype = input_dtype

    def to_embedding_model(
        self,
        layer_name: Optional[str] = None,
        freeze: Union[bool, List[str]] = False,
        projection_head: Optional[nn.Module] = None,
    ) -> nn.Module:
        """Convert a general model from :py:attr:`.model` to an embedding model.

        :param layer_name: the name of the layer that is used for output embeddings.
            All layers *after* that layer will be removed. When set to ``None``, then
            the last layer listed in :py:attr:`.embedding_layers` will be used. To see
            all available names you can check ``name`` field of
            :py:attr:`.embedding_layers`.
        :param freeze: if set as True, will freeze all layers before
            :py:`attr`:`layer_name`. If set as list of str, will freeze layers by names.
        :param projection_head: Attach a module at the end of model, this module should
            be always trainable.
        :return: Converted embedding model.
        """

        model = copy.deepcopy(self._model)
        _all_embed_layers = {layer['name']: layer for layer in self.embedding_layers}
        if layer_name:
            try:
                _embed_layer = _all_embed_layers[layer_name]
            except KeyError as e:
                raise KeyError(
                    f'`embedding_layer_name` must be one of {_all_embed_layers.keys()}'
                    f', given {layer_name}'
                ) from e
        else:
            # when not given, using the last layer
            _embed_layer = self.embedding_layers[-1]

        if isinstance(freeze, list):
            # freeze specific layers defined in `freeze_layers`
            for layer_name, param in zip(_all_embed_layers, model.parameters()):
                if layer_name in freeze:
                    param.requires_grad = False
        elif isinstance(freeze, bool) and freeze is True:
            # freeze all layers, not including bottleneck module
            for param in model.parameters():
                param.requires_grad = False

        _embed_layer_output_shape = 0
        _relative_idx_to_embedding_layer = None
        for name, module in model.named_modules():
            if name == _embed_layer['module_name']:
                _relative_idx_to_embedding_layer = 0
                _embed_layer_output_shape = _embed_layer['output_shape']
            if (
                _relative_idx_to_embedding_layer
                and _relative_idx_to_embedding_layer >= 1
            ):
                replaced_layer = nn.Identity(_embed_layer_output_shape)
                if '.' in name:
                    # Note: in torchvision, nested layer names are named with '.'
                    # e.g. classifier.0
                    nested_module, layer = name.split('.')
                    setattr(getattr(model, nested_module), layer, replaced_layer)
                else:
                    setattr(model, name, replaced_layer)

            if _relative_idx_to_embedding_layer is not None:
                _relative_idx_to_embedding_layer += 1

        if projection_head:
            embed_model_with_projection_head = nn.Sequential()
            embed_model_with_projection_head.add_module('embed_model', model)
            embed_model_with_projection_head.add_module(
                'projection_head', projection_head
            )
            return embed_model_with_projection_head

        return model

    @property
    def embedding_layers(self) -> List[dict]:
        """Get all dense layers that can be used as embedding layer from the
        :py:attr:`.model`.

        :return: layers info list of dicts.
        """
        _layers = self.summary()
        return [_l for _l in _layers if _l['is_embedding_layer']]

    def summary(self, skip_identity_layer: bool = False) -> List[dict]:
        """Interpret the DNN model and produce model information.

        :param skip_identity_layer: If skip identity layer.
        :return: The model information stored as list of dicts.
        """
        if not self._input_shape:
            raise ValueError(
                f'{self.__class__} requires a valid `input_shape`, but receiving '
                f'{self._input_shape}'
            )

        user_model = copy.deepcopy(self._model)
        dtypes = [getattr(torch, self._input_dtype)] * len(self._input_shape)
        depth = len(list(user_model.modules()))
        for name, module in user_model.named_modules():
            module.name = name

        def _get_shape(output):
            output_shape = None
            if output is not None:
                if isinstance(output, (list, tuple)):
                    output_shape = [
                        _get_shape(o) for o in output if isinstance(o, torch.Tensor)
                    ]
                    if len(output_shape) == 1:
                        output_shape = output_shape[0]
                elif isinstance(output, torch.Tensor):
                    output_shape = list(output.shape)

            return output_shape

        def register_hook(module):
            def hook(module, input, output):
                input_shape = _get_shape(input)
                output_shape = _get_shape(output)

                if input_shape and output_shape:
                    class_name = str(module.__class__).split('.')[-1].split("'")[0]

                    module_idx = len(summary)

                    m_key = f'{class_name.lower()}_{module_idx + 1}'
                    summary[m_key] = OrderedDict()
                    summary[m_key]['cls_name'] = module.__class__.__name__
                    summary[m_key]['name'] = m_key
                    summary[m_key]['output_shape'] = output_shape
                    summary[m_key]['input_shape'] = input_shape
                    summary[m_key]['module_name'] = module.name

                    params = 0
                    summary[m_key]['trainable'] = False
                    if hasattr(module, 'weight') and hasattr(module.weight, 'size'):
                        params += np.prod(list(module.weight.size()))
                        summary[m_key]['trainable'] = module.weight.requires_grad
                    if hasattr(module, 'bias') and hasattr(module.bias, 'size'):
                        params += np.prod(list(module.bias.size()))
                    if hasattr(module, 'all_weights'):
                        params += sum(
                            np.prod(ww.size()) for w in module.all_weights for ww in w
                        )

                    summary[m_key]['nb_params'] = params

            if (
                not isinstance(module, nn.Sequential)
                and not isinstance(module, nn.ModuleList)
                and (module != user_model or depth < 1)
            ):
                hooks.append(module.register_forward_hook(hook))

        device = next(user_model.parameters()).device
        x = [
            torch.randint(0, 2, (2, *in_shape), device=device, dtype=dt)
            for in_shape, dt in zip(self._input_shape, dtypes)
        ]

        # create properties
        summary = OrderedDict()
        hooks = []

        # register hook
        user_model.apply(register_hook)

        # make a forward pass
        user_model(*x)

        # remove these hooks
        for h in hooks:
            h.remove()

        results = []
        for idx, layer in enumerate(summary):
            output_shape = summary[layer]['output_shape']
            input_shape = summary[layer]['input_shape']
            is_embedding_layer = not (
                not output_shape
                or not is_seq_int(output_shape)
                or summary[layer]['cls_name'] == self._model.__class__.__name__
            )

            if (
                skip_identity_layer
                and output_shape == input_shape
                and not summary[layer]['nb_params']
            ):
                # not an effective layer, often a wrapper/identity layer
                continue

            results.append(
                {
                    **summary[layer],
                    'output_features': output_shape[-1],
                    'output_shape_display': output_shape[1:],
                    'layer_idx': idx,
                    'is_embedding_layer': is_embedding_layer,
                }
            )

        return results
