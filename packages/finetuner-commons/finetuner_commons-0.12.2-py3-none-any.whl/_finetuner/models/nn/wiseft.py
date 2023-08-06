from typing import Union

from torch import nn

from _finetuner.excepts import KeysMismatchError


def apply_wiseft(
    pretrained: nn.Module,
    fine_tuned: nn.Module,
    alpha: Union[int, float] = 0.4,
) -> nn.Module:
    """Merge weights from pretrained to fine-tuned model.

    Source: Mitchell et al. Robust fine-tuning of zero-shot models

    :param pretrained: The pretrained model build from model builder.
    :param fine_tuned: The fine-tuned model produced from finetuner.
    :param alpha: The coefficient controls the weights between pretrained model and
        fine-tuned model. If `alpha` set to 0, fully use pretrained weights,
        if `alpha` set to 1, fully use fine-tuned model.
    """
    theta_0 = pretrained.state_dict()
    theta_1 = fine_tuned.state_dict()
    if not set(theta_0.keys()) == set(theta_1.keys()):
        raise KeysMismatchError(
            'Pre-trained model weight mismatch against fine-tuned model weights.'
        )
    if alpha > 1 or alpha < 0:
        raise ValueError(
            f'Alpha must be greater equal than 0 and lower equal than 1, '
            f'got {alpha} instead.'
        )
    theta = {
        key: (1 - alpha) * theta_0[key] + alpha * theta_1[key] for key in theta_0.keys()
    }
    fine_tuned.load_state_dict(theta)
    return fine_tuned
