import json
from dataclasses import asdict
from typing import Any, Dict, TextIO, Type, TypeVar

import yaml
from pydantic import BaseModel

BaseModelT = TypeVar('BaseModelT', bound=BaseModel)


def dataclass_to_dict(obj: Any) -> Dict[str, Any]:
    """Serialize a dataclass object to a dictionary."""
    return asdict(obj)


def pydantic_to_dict(obj: BaseModel) -> Dict[str, Any]:
    """Serialize a pydantic object to a dictionary."""
    return obj.dict()


def pydantic_from_dict(d: Dict[str, Any], model_class: Type[BaseModelT]) -> BaseModelT:
    return model_class.parse_obj(d)


def to_json(d: Dict[str, Any], f: TextIO) -> None:
    """Dump a dictionary to a JSON stream."""
    json.dump(d, f, indent=2)


def to_yaml(d: Dict[str, Any], f: TextIO) -> None:
    """Dump a dictionary to a YAML stream."""
    yaml.safe_dump(d, f, sort_keys=False)


def from_json(f: TextIO) -> Dict[str, Any]:
    """Load dictionary object from a JSON stream."""
    return json.load(f)


def from_yaml(f: TextIO) -> Dict[str, Any]:
    """Load dictionary object from a YAML stream."""
    return yaml.safe_load(f)
