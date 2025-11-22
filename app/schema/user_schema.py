from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: Optional[EmailStr]
    password: str

class UserRead(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr]
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
