from sqlalchemy.orm import Session
from ..models.supplier_model import Supplier
from ..schema.supplier_schema import SupplierCreate
from ..utils.excel_exporter import export_to_excel

class SupplierService:
    def get_all_suppliers(db: Session):
        return db.query(Supplier).all()

    def create_supplier(db: Session, data: SupplierCreate):
        supplier = Supplier(**data.dict())
        db.add(supplier)
        db.commit()
        db.refresh(supplier)
        return supplier
   
    def export_suppliers(db: Session):
        suppliers = db.query(Supplier).all()

        headers = ["ID", "Name", "Email", "Phone"]
        rows = [
            [s.id, s.name, s.email, s.phone] for s in suppliers
        ]

        return export_to_excel(headers, rows)