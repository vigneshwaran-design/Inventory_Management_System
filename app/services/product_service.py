from sqlalchemy.orm import Session
from ..models.product_model import Product
from ..schema.product_schema import ProductCreate, ProductUpdate
from ..utils.excel_exporter import export_to_excel

class ProductService:
    
    def getbyID(db: Session, product_id: int):
        """Get one product by ID."""
        return db.query(Product).filter(Product.id == product_id).first()
    def get_all_products(db: Session):
        return db.query(Product).all()

    def create_product(db: Session, data: ProductCreate):
        product = Product(**data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    def update_product(db: Session, product_id: int, data: ProductUpdate):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            return None

        for key, value in data.dict(exclude_unset=True).items():
            setattr(product, key, value)

        db.commit()
        db.refresh(product)
        return product

    def delete_product(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()
        return product
    
    def export_low_stock(db: Session):
        low_stock = db.query(Product).filter(Product.quantity < 10).all()

        headers = ["ID", "Product_Code", "Name", "Quantity", "Category"]
        rows = [
            [p.id, p.product_code, p.name, p.quantity, p.category.name if p.category else ""]
            for p in low_stock
        ]

        return export_to_excel(headers, rows)