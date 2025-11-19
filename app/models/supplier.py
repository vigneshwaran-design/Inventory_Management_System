from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

class Supplier(Base):
    __tablename__ = "Supplier"

    Supplier_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String, nullable=False)
    ContactNo = Column(String, nullable=True)

    # Reverse relationship
    products = relationship("Product", back_populates="supplier")
