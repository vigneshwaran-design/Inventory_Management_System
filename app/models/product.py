from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Product(Base):
    __tablename__ = "Product"

    Product_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String, nullable=False)
    Quantity = Column(Integer, nullable=False, default=0)
    IsActive = Column(Boolean, default=True)

    Category_ID = Column(Integer, ForeignKey("Category.Category_ID"))
    Supplier_ID = Column(Integer, ForeignKey("Supplier.Supplier_ID"))

    category = relationship("Category")
    supplier = relationship("Supplier")
