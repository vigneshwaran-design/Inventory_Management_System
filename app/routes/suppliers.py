from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from ..database import get_db
from ..schema.supplier_schema import SupplierCreate, SupplierRead
from ..services.supplier_service import SupplierService
from typing import List
from ..core.deps import get_current_user


router = APIRouter()

@router.post("/", response_model=SupplierRead)
def create_supplier(payload: SupplierCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    return SupplierService.create_supplier(db, payload)

@router.get("/", response_model=List[SupplierRead])
def get_suppliers(db: Session = Depends(get_db),current_user: str = Depends(get_current_user)):
    return SupplierService.get_all_suppliers(db)

@router.get("/suppliers/export")
def export_suppliers(db: Session = Depends(get_db)):
    excel_file = SupplierService.export_suppliers(db)

    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=suppliers.xlsx"}
    )