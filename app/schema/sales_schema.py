from pydantic_settings import BaseModel
from datetime import datetime
from typing import Optional

class SaleCreate(BaseModel):
    product_id: int
    quantity: int

class SaleResponse(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: float
    created_at: datetime

    class Config:
        orm_mode = True
