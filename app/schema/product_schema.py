from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductCreate(BaseModel):
    product_code: str
    name: str
    description: Optional[str]
    price: float
    quantity: int
    category_id: Optional[int]
    supplier_id: Optional[int]

class ProductUpdate(BaseModel):
    product_code: Optional[str]
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    quantity: Optional[int]
    category_id: Optional[int]
    supplier_id: Optional[int]

class ProductRead(ProductCreate):
    id: int
    active: bool
    created_at: datetime

    class Config:
        orm_mode = True
