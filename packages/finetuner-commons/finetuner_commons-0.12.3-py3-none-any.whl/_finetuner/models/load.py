import io
import logging
import os
import zipfile
from typing import Any, Dict, Optional, Tuple, Union
from zipfile import ZipFile

import hubble
import yaml

from _finetuner.excepts import (
    ArtifactNotFound,
    CorruptedArtifact,
    CorruptedMetadata,
    NoSuchModel,
    SelectModelRequired,
)

MODEL_DUMP_FNAME = 'model'
MODEL_METADATA_FNAME = 'metadata.yml'

logger = logging.getLogger(__name__)


def _load_artifact_from_dir(
    artifact: str, export_type: str = 'pt'
) -> Dict[str, Tuple[io.BytesIO, Union[str, io.BytesIO]]]:
    """
    Load artifact buffers from local dir.
    """

    _models2buffers: Dict[str, Tuple[io.BytesIO, Union[str, io.BytesIO]]] = {}
    _model_name = MODEL_DUMP_FNAME + '.' + export_type

    for _root, dirs, files in os.walk(artifact):
        if _model_name in files and MODEL_METADATA_FNAME in files:
            _metadata_stream = io.BytesIO()
            with open(os.path.join(_root, MODEL_METADATA_FNAME), 'rb') as f:
                _metadata_stream.write(f.read())

            _models2buffers[_root] = (
                _metadata_stream,
                os.path.join(_root, _model_name),
            )

    return _models2buffers


def _read_local_zipfile(fname: str) -> io.BytesIO:
    """
    Read local zipfile to a buffer.
    """
    zbuffer = io.BytesIO()
    with open(fname, 'rb') as f:
        zbuffer.write(f.read())

    return zbuffer


def _pull_remote_artifact(artifact_id: str, token: Optional[str] = None) -> io.BytesIO:
    """
    Pull artifact from Hubble.
    """
    zbuffer = io.BytesIO()
    client = hubble.Client(jsonify=False, token=token)
    try:
        _ = client.download_artifact(id=artifact_id, f=zbuffer)
    except Exception as exc:
        raise ArtifactNotFound(f'Artifact {artifact_id} not found, details: {str(exc)}')

    return zbuffer


def _load_artifact_from_zipfile(
    artifact: str,
    zbuffer: io.BytesIO,
    export_type: str = 'pt',
) -> Dict[str, Tuple[io.BytesIO, Union[str, io.BytesIO]]]:
    """
    Load artifact buffers from zipfile.
    """

    _models2buffers: Dict[str, Tuple[io.BytesIO, Union[str, io.BytesIO]]] = {}
    _model_name = MODEL_DUMP_FNAME + '.' + export_type

    zbuffer.seek(0)
    zf: ZipFile
    try:
        zf = ZipFile(zbuffer, mode='r', allowZip64=True)
    except zipfile.BadZipfile:
        raise CorruptedArtifact(f'Not a zip file: {artifact}')

    paths = zf.namelist()
    _intermediate_models2buffers = {}
    for path in paths:
        *header, tail = path.split('/')
        if tail == MODEL_METADATA_FNAME:
            prefix = '/'.join(header)
            _intermediate_models2buffers[prefix] = io.BytesIO(zf.read(path))

    for path in paths:
        *header, tail = path.split('/')
        prefix = '/'.join(header)
        if tail == _model_name and prefix in _intermediate_models2buffers:
            _metadata_stream = _intermediate_models2buffers[prefix]
            _models2buffers[prefix] = (
                _metadata_stream,
                io.BytesIO(zf.read(path)),
            )

    return _models2buffers


def load_artifact(
    artifact: str,
    is_onnx: bool = False,
    select_model: Optional[str] = None,
    token: Optional[str] = None,
) -> Tuple[str, Dict[str, Any], Union[str, io.BytesIO]]:
    """
    Load the artifact either from a directory, a zip file or directly from
    Hubble.
    """

    _models2buffers: Dict[str, Tuple[io.BytesIO, Union[str, io.BytesIO]]]
    export_type = 'onnx' if is_onnx else 'pt'
    _model_name = MODEL_DUMP_FNAME + '.' + export_type

    if os.path.isdir(artifact):
        logger.info(f'Loading from local dir: \'{artifact}\'')
        _models2buffers = _load_artifact_from_dir(artifact, export_type)
    else:
        if os.path.isfile(artifact):
            logger.info(f'Loading from local file: \'{artifact}\'')
            zbuffer = _read_local_zipfile(artifact)
        else:
            logger.info(f'Pulling from Jina AI Cloud: {artifact}')
            zbuffer = _pull_remote_artifact(artifact, token)

        _models2buffers = _load_artifact_from_zipfile(artifact, zbuffer, export_type)

    if len(_models2buffers) == 0:
        raise CorruptedArtifact(
            'Could not locate any directory with the '
            f'\'{MODEL_METADATA_FNAME}\' and \'{_model_name}\' files'
        )

    _model_metadata: Dict[str, Dict[str, Any]] = {}
    _model_dumps: Dict[str, Union[str, io.BytesIO]] = {}

    for prefix, (_meta_stream, _model_dump) in _models2buffers.items():

        _meta_stream.seek(0)
        try:
            metadata = yaml.safe_load(_meta_stream)
        except Exception as exc:
            raise CorruptedMetadata(
                f'Metadata found in {prefix} are corrupted, details: {str(exc)}'
            )

        _meta_stream.close()

        name = metadata.get('name')
        if name is None:
            raise CorruptedMetadata(f'Field \'name\' is missing from {prefix}')

        _model_metadata[name] = metadata
        _model_dumps[name] = _model_dump

    logger.info(f'Found models: {list(_model_metadata.keys())}')

    if select_model:
        if select_model not in _model_metadata:
            raise NoSuchModel(f'No model named \'{select_model}\' in artifact')
        model_name = select_model
    else:
        if len(_model_metadata) > 1:
            raise SelectModelRequired(
                'Found more than 1 models in artifact, please select model '
                'using `select_model`'
            )
        model_name = list(_model_metadata.keys())[0]

    model_metadata = _model_metadata[model_name]
    model_dump = _model_dumps[model_name]

    return model_name, model_metadata, model_dump
