from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import SupplierCreate, SupplierUpdate, SupplierResponse
from app.services import SupplierService

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.post("/", response_model=SupplierResponse)
def create_supplier(data: SupplierCreate, db: Session = Depends(get_db)):
    return SupplierService.create(db, data)

@router.get("/", response_model=list[SupplierResponse])
def get_suppliers(db: Session = Depends(get_db)):
    return SupplierService.get_all(db)

@router.put("/{id}", response_model=SupplierResponse)
def update_supplier(id: int, data: SupplierUpdate, db: Session = Depends(get_db)):
    return SupplierService.update(db, id, data)
