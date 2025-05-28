from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class UsersViewModel(BaseModel):
    admin: bool
    email: str
    name: str
    phone: str
    password_hash: bytes
    restaurant: bool
    created_at: datetime
    updated_at: datetime
