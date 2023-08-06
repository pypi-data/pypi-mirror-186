from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

from caronte_common.types.db_field import FieldConfigFunction


T = TypeVar("T")


@dataclass
class FieldConfig:
    field_name: str
    params: dict
    config_type: FieldConfigFunction


@dataclass
class Document(Generic[T]):
    field_config: List[FieldConfig]
    config: dict
    name: str
    instance: Optional[T] = None
