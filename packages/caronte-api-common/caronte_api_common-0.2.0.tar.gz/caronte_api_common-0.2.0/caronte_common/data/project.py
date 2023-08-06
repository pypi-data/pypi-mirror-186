from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

from caronte_common.data.claim import Claim
from caronte_common.data.config import Config
from caronte_common.data.role import Role
from caronte_common.data.user import User


@dataclass
class Project:
    name: str
    description: str
    config: Optional[Config] = None
    owner: Optional[User] = None
    claims: Optional[List[Claim]] = None
    roles: Optional[List[Role]] = None
    users: Optional[List[User]] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    external_id: Optional[UUID] = None
