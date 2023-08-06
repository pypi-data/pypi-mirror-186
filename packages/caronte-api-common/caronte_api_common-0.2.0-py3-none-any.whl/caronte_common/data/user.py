from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from uuid import UUID


@dataclass
class User:
    email: str
    cellphone: str
    user_name: str
    full_name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    password: Optional[str] = None
    external_id: Optional[UUID] = None
