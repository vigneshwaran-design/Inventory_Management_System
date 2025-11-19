from sqlalchemy.orm import Session
from app.models import Supplier
from app.schema import SupplierCreate, SupplierUpdate

class SupplierService:

    @staticmethod
    def create(db: Session, data: SupplierCreate):
        supplier = Supplier(**data.dict())
        db.add(supplier)
        db.commit()
        db.refresh(supplier)
        return supplier

    @staticmethod
    def get_all(db: Session):
        return db.query(Supplier).all()

    @staticmethod
    def update(db: Session, id: int, data: SupplierUpdate):
        supplier = db.query(Supplier).filter(Supplier.Supplier_ID == id).first()
        if not supplier:
            return None
        for field, value in data.dict(exclude_unset=True).items():
            setattr(supplier, field, value)
        db.commit()
        db.refresh(supplier)
        return supplier
