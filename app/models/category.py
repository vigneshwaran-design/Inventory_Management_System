from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Category(Base):
    __tablename__ = "Category"

    Category_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String, nullable=False)
    IsActive = Column(Boolean, default=True)

    # Reverse relationship
    products = relationship("Product", back_populates="category")
