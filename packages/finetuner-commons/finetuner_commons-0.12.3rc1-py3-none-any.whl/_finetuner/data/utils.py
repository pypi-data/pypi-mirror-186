from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Tuple, Union

import torch
from docarray import Document
from torch.utils.data._utils.collate import default_collate

from _finetuner.data.collate import BaseCollate, DefaultCollate
from _finetuner.data.preprocess import BasePreprocess, DefaultPreprocess

if TYPE_CHECKING:
    from docarray.typing import DocumentContentType

    #: The type of preprocessing function
    PreprocessFnType = Union[BasePreprocess, Callable[[Document], DocumentContentType]]

    #: The type of collate function
    CollateFnType = Union[
        BaseCollate,
        Callable[
            [List[DocumentContentType]],
            Any,
        ],
    ]


__default_modality_key__ = 'input'


class PreprocessCollateWrapper:
    """
    This helper class wraps the preprocess and collate functions, that are provided
    by the user and are defined on single modalities, and exposes new preprocess-all
    and collate-all functions that can work on either single-modal or multi-modal
    cases. The class also handles the resolution of the input preprocess and collate
    functions.
    """

    def __init__(
        self,
        preprocess_fn: Union[
            Optional['PreprocessFnType'], Dict[str, Optional['PreprocessFnType']]
        ],
        collate_fn: Union[
            Optional['CollateFnType'], Dict[str, Optional['CollateFnType']]
        ],
        multi_modal: bool = False,
    ) -> None:
        """Constructor."""
        self._preprocess_fns: Dict[str, Optional['CollateFnType']]
        self._collate_fns: Dict[str, Optional['CollateFnType']]

        self._preprocess_fns, self._collate_fns = self.resolve(
            preprocess_fn, collate_fn
        )

        # This will be a list of unique elements since it is derived from a dict
        # Also the order will be preserved
        self._modalities = list(self._preprocess_fns.keys())

        if not multi_modal and len(self._modalities) > 1:
            raise ValueError(
                'You need to set multi_modal to True in order to process '
                f'{len(self._modalities)} modalities'
            )

        self._preprocess: Callable = (
            self._multi_modal_preprocess
            if multi_modal
            else self._single_modal_preprocess
        )

    def _single_modal_preprocess(
        self, doc: Document
    ) -> Dict[str, 'DocumentContentType']:
        """
        Document preprocess method for single modality cases.
        """
        return {  # this will always have a length of 1
            modality: func(doc) for modality, func in self._preprocess_fns.items()
        }

    def _multi_modal_preprocess(
        self, doc: Document
    ) -> Dict[str, 'DocumentContentType']:
        """
        Document preprocess method for multiple modality cases.
        """
        if len(doc.chunks) < len(self._modalities):
            raise ValueError(
                f'Found doc: {doc.id} with {len(doc.chunks)} chunks, expected '
                f'modalities are {len(self._modalities)}'
            )

        chunks_modalities = [chunk.modality for chunk in doc.chunks]
        if set(self._modalities).issubset(chunks_modalities):
            # resolve which chunk goes to which preprocess function using the
            # .modality attribute
            return {
                modality: func(
                    next(filter(lambda x: x.modality == modality, doc.chunks))
                )
                for modality, func in self._preprocess_fns.items()
            }

        # resolve which chunk goes to which preprocess function using the index,
        # i.e. first chunk goes to the first modality defined etc
        return {
            modality: func(doc.chunks[i])
            for i, (modality, func) in enumerate(self._preprocess_fns.items())
        }

    @property
    def modalities(self) -> List[str]:
        """
        Get the input modalities.
        """
        return self._modalities

    def preprocess(self, doc: Document) -> Dict[str, 'DocumentContentType']:
        """
        Exposed preprocess method. Wraps per-modality preprocess functions to a single
        preprocess function.
        """
        return self._preprocess(doc)

    def collate_contents(
        self, batch: List[Dict[str, 'DocumentContentType']]
    ) -> Dict[str, torch.Tensor]:
        """
        Exposed collate method for contents only.
        """
        return {
            modality: collate_fn([content[modality] for content in batch])
            for modality, collate_fn in self._collate_fns.items()
        }

    @staticmethod
    def collate_labels(batch: List[int]) -> torch.Tensor:
        """
        Exposed collate method for labels only.
        """
        return default_collate(batch)

    def collate(
        self, batch: List[Tuple[Dict[str, 'DocumentContentType'], int]]
    ) -> Tuple[Dict[str, torch.Tensor], torch.Tensor]:
        """
        Exposed collate method. Wraps per-modality collate functions to a single
        collate function.
        """
        contents, labels = zip(*batch)
        return self.collate_contents(contents), self.collate_labels(labels)

    @staticmethod
    def resolve(
        preprocess_fn: Union[
            Optional['PreprocessFnType'], Dict[str, Optional['PreprocessFnType']]
        ],
        collate_fn: Union[
            Optional['CollateFnType'], Dict[str, Optional['CollateFnType']]
        ],
    ) -> Tuple[Dict[str, 'PreprocessFnType'], Dict[str, 'CollateFnType']]:
        """
        Resolves the user provided preprocess and collate functions. The goal of this
        function is to have the resolution and the checking of the user provided
        preprocess and collate functions as well as the falling back to defaults, in one
        place. Given the user provided preprocess and collate functions, which can
        be functions or dicts, this method tries to resolve missing keys, incosistent
        keys as well as falling back to defaults when necessary.
        """
        preprocess_fns: Dict[str, 'PreprocessFnType']
        collate_fns: Dict[str, 'CollateFnType']

        if preprocess_fn is None:
            preprocess_fns = {__default_modality_key__: DefaultPreprocess()}
        elif isinstance(preprocess_fn, dict):
            if len(preprocess_fn) == 0:
                raise ValueError('Got an empty dict of preprocess functions')
            else:
                preprocess_fns = {
                    modality: func or DefaultPreprocess()
                    for modality, func in preprocess_fn.items()
                }
        else:
            preprocess_fns = {__default_modality_key__: preprocess_fn}

        if collate_fn is None:
            collate_fns = {__default_modality_key__: DefaultCollate()}
        elif isinstance(collate_fn, dict):
            if len(collate_fn) == 0:
                raise ValueError('Got an empty dict of collate functions')
            else:
                collate_fns = {
                    modality: func or DefaultCollate()
                    for modality, func in collate_fn.items()
                }
        else:
            collate_fns = {__default_modality_key__: collate_fn}

        preprocess_modalities = set(preprocess_fns.keys())
        collate_modalities = set(collate_fns.keys())

        if preprocess_modalities != collate_modalities:
            raise ValueError(
                f'Got different modalities for preprocess and collate functions, '
                f'{preprocess_modalities} != {collate_modalities}'
            )

        return preprocess_fns, collate_fns
