from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class Claim:
    name: str
    value: Union[str, int, float]
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
