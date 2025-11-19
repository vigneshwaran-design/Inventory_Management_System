from pydantic import BaseModel
from typing import Optional
from .category import CategoryResponse
from .supplier import SupplierResponse


class ProductBase(BaseModel):
    Name: str
    Quantity: int
    IsActive: bool = True

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    Category_ID: int
    Supplier_ID: int


class ProductUpdate(BaseModel):
    Name: Optional[str] = None
    Quantity: Optional[int] = None
    IsActive: Optional[bool] = None
    Category_ID: Optional[int] = None
    Supplier_ID: Optional[int] = None


class ProductResponse(ProductBase):
    Product_ID: int
    Category_ID: Optional[int] = None
    Supplier_ID: Optional[int] = None
    category: Optional[CategoryResponse] = None
    supplier: Optional[SupplierResponse] = None

    class Config:
        orm_mode = True
