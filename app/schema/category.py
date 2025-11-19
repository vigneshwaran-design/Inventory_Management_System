from pydantic import BaseModel

class CategoryBase(BaseModel):
    Name: str
    IsActive: bool = True
    
    class Config:
        orm_mode = True

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    Name: str | None = None
    IsActive: bool | None = None

class CategoryResponse(CategoryBase):
    Category_ID: int

    class Config:
        orm_mode = True
