from sqlalchemy.orm import Session
from ..models.category_model import Category
from ..schema.category_schema import CategoryCreate
from ..utils.excel_exporter import export_to_excel
class CategoryService:
    @staticmethod
    def get_all_categories(db: Session):
        return db.query(Category).all()

    @staticmethod
    def create_category(db: Session, data: CategoryCreate):
        category = Category(**data.dict())
        db.add(category)
        db.commit()
        db.refresh(category)
        return category
    
    def export_categories(db: Session):
        categories = db.query(Category).all()
        
        headers = ["ID", "Category Name", "Description"]
        rows = [
            [cat.id, cat.name, cat.description or ""] 
            for cat in categories
        ]
        
        return export_to_excel(headers, rows)
