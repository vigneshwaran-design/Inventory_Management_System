from sqlalchemy.orm import Session
from app.models import Product
from app.schema import ProductCreate, ProductUpdate
from sqlalchemy.orm import joinedload

class ProductService:

    @staticmethod
    def create(db: Session, data: ProductCreate):
        product = Product(**data.dict())
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def get_all(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get(db: Session, product_id: int):
     print("product_id", product_id)
     return (
        db.query(Product)
        .options(
            joinedload(Product.category),
            joinedload(Product.supplier)
        )
        .filter(Product.Product_ID == product_id)
        .first()
    )


    @staticmethod
    def update(db: Session, product_id: int, data: ProductUpdate):
        product = db.query(Product).filter(Product.Product_ID == product_id).first()
        if not product:
            return None

        for field, value in data.dict(exclude_unset=True).items():
            setattr(product, field, value)

        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def delete(db: Session, product_id: int):
        product = db.query(Product).filter(Product.Product_ID == product_id).first()
        if not product:
            return False

        db.delete(product)
        db.commit()
        return True
