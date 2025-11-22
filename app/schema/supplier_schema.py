from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class SupplierCreate(BaseModel):
    name: str
    contact_email: Optional[EmailStr]
    phone: Optional[str]
    address: Optional[str]

class SupplierRead(SupplierCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
