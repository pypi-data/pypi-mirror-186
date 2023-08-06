from dataclasses import dataclass
from typing import List, Optional

from caronte_common.data.claim import Claim


@dataclass
class Role:
    name: str
    claims: List[Claim]
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
