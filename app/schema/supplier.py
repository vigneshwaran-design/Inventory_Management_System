from pydantic import BaseModel

class SupplierBase(BaseModel):
    Name: str
    ContactNo: int | None = None
    
    class Config:
        orm_mode = True

class SupplierCreate(SupplierBase):
    pass

class SupplierUpdate(BaseModel):
    Name: str | None = None
    ContactNo: int | None = None

class SupplierResponse(SupplierBase):
    Supplier_ID: int

    class Config:
        orm_mode = True
