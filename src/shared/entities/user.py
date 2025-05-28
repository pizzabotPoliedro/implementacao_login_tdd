from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    admin: bool = False
    email: str
    name: str
    phone: str
    password_hash: bytes
    restaurant: bool = False
    image: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
