import io
import os
from dataclasses import dataclass
from typing import IO, Any, ClassVar, Dict, List, Tuple
from zipfile import ZIP_DEFLATED, ZipFile

import hubble
from torch import nn

from _finetuner.runner.helper import dataclass_to_dict, pydantic_to_dict, to_yaml
from _finetuner.runner.model import RunnerModel
from _finetuner.runner.stubs.config import RunConfig


@dataclass
class RunMetadata:
    """This class reperesents some run metadata."""

    name: str
    experiment: str
    device: str
    duration: str
    timestamp: str
    finetuner_version: str
    model_type: str
    product: str = 'finetuner'


@dataclass
class RunArtifact:
    """
    This class represents the output of a finetuner run and implements methods
    for storing locally and uploading to Hubble.
    """

    run_config: RunConfig
    run_metadata: RunMetadata
    metrics: Dict[str, Dict[str, float]]
    models: Dict[str, RunnerModel]
    modules: Dict[str, nn.Module]
    input_map: Dict[str, List[str]]

    _models_dir: ClassVar[str] = 'models'
    _run_config_fname: ClassVar[str] = 'config.yml'
    _metadata_fname: ClassVar[str] = 'metadata.yml'
    _metrics_fname: ClassVar[str] = 'metrics.yml'
    _input_map_fname: ClassVar[str] = 'input-map.yml'
    _model_dump_fname: ClassVar[str] = 'model'

    def _to_buffers(self) -> Dict[str, IO]:
        """
        Dump artifact components to in-memory buffers.
        """
        _f_config = io.StringIO()
        to_yaml(pydantic_to_dict(self.run_config), _f_config)

        _f_metadata = io.StringIO()
        to_yaml(dataclass_to_dict(self.run_metadata), _f_metadata)

        _f_metrics = io.StringIO()
        to_yaml(self.metrics, _f_metrics)

        _f_inputmap = io.StringIO()
        to_yaml(self.input_map, _f_inputmap)

        buffers = {
            self._run_config_fname: _f_config,
            self._metadata_fname: _f_metadata,
            self._metrics_fname: _f_metrics,
            f'{self._models_dir}/{self._input_map_fname}': _f_inputmap,
        }
        model: RunnerModel
        model_format = 'onnx' if self.run_config.model.to_onnx else 'pt'
        for name, model in self.models.items():
            _f_model_metadata = io.StringIO()
            to_yaml(model.metadata, _f_model_metadata)
            buffers[
                f'{self._models_dir}/{name}/{self._metadata_fname}'
            ] = _f_model_metadata

            _f_model_dump = io.BytesIO()
            model.export(
                model=self.modules[name],
                f=_f_model_dump,
                to_onnx=self.run_config.model.to_onnx,
            )
            buffers[
                f'{self._models_dir}/{name}/{self._model_dump_fname}.{model_format}'
            ] = _f_model_dump

        return buffers

    def _to_zipfile(self) -> io.BytesIO:
        """
        Dump state to a zip file.
        """
        buffers = self._to_buffers()
        zbuffer: io.BytesIO = io.BytesIO()
        with ZipFile(
            zbuffer, mode='a', compression=ZIP_DEFLATED, allowZip64=True
        ) as zf:
            for name, buffer in buffers.items():
                buffer.seek(0)
                zf.writestr(self.run_config.run_name + '/' + name, buffer.read())
                buffer.close()

            del buffers

        return zbuffer

    def save(self, directory: str = './', zipped: bool = False) -> int:
        """
        Save state to disk.
        """
        os.makedirs(directory, exist_ok=True)

        if zipped:
            zbuffer = self._to_zipfile()
            size = zbuffer.tell()

            zbuffer.seek(0)
            with open(
                os.path.join(directory, self.run_config.run_name + '.zip'), 'wb'
            ) as f:
                f.write(zbuffer.read())
            zbuffer.close()
            del zbuffer

            return size

        root = os.path.join(directory, self.run_config.run_name)
        os.makedirs(root, exist_ok=False)

        buffers = self._to_buffers()
        size = 0

        for name, buffer in buffers.items():

            size += buffer.tell()

            fpath = os.path.join(root, name)
            head, _ = os.path.split(fpath)
            os.makedirs(head, exist_ok=True)

            buffer.seek(0)
            _file_rights = 'w' if isinstance(buffer, io.StringIO) else 'wb'
            with open(fpath, _file_rights) as f:
                f.write(buffer.read())
            buffer.close()

        del buffers

        return size

    def push(
        self, artifact_id: str, public: bool = False
    ) -> Tuple[int, Dict[str, Any]]:
        """
        Push to Hubble.
        """
        zbuffer = self._to_zipfile()
        size = zbuffer.tell()

        zbuffer.seek(0)

        client = hubble.Client(jsonify=True)
        resp = client.upload_artifact(
            f=zbuffer,
            id=artifact_id,
            metadata=dataclass_to_dict(self.run_metadata),
            is_public=public,
        )
        zbuffer.close()
        del zbuffer

        return size, resp
