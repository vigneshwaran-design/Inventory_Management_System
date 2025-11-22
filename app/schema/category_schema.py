from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str]

class CategoryRead(CategoryCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
