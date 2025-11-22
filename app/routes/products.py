from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse

from typing import List

from ..database import get_db
from ..schema.product_schema import ProductCreate, ProductRead, ProductUpdate
from ..services.product_service import ProductService
from ..core.deps import get_current_user

router = APIRouter()

@router.post("/", response_model=ProductRead)
def create_product(
    payload: ProductCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return ProductService.create_product(db, payload)

@router.get("/", response_model=List[ProductRead])
def get_all_products(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return ProductService.get_all_products(db)

@router.get("/{product_id}", response_model=ProductRead)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    product = ProductService.getbyID(db, product_id)
    if not product:
        raise HTTPException(404, "Product not found")
    return product

@router.put("/{product_id}", response_model=ProductRead)
def update_product(
    product_id: int,
    payload: ProductUpdate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return ProductService.update_product(db, product_id, payload)

@router.delete("/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return ProductService.delete_product(db, product_id)

@router.get("/products/low-stock/export")
def export_low_stock(db: Session = Depends(get_db)):
    excel_file = ProductService.export_low_stock(db)
    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=low_stock_items.xlsx"}
    )
