from sqlalchemy.orm import Session
from app.models import Category
from app.schema import CategoryCreate, CategoryUpdate

class CategoryService:

    @staticmethod
    def create(db: Session, data: CategoryCreate):
        category = Category(**data.dict())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category

    @staticmethod
    def get_all(db: Session):
        return db.query(Category).all()

    @staticmethod
    def update(db: Session, id: int, data: CategoryUpdate):
        category = db.query(Category).filter(Category.Category_ID == id).first()
        if not category:
            return None
        for field, value in data.dict(exclude_unset=True).items():
            setattr(category, field, value)
        db.commit()
        db.refresh(category)
        return category
