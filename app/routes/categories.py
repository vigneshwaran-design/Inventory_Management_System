from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from typing import List

from ..database import get_db
from ..schema.category_schema import CategoryCreate, CategoryRead
from ..services.category_service import CategoryService
from ..core.deps import get_current_user

router = APIRouter()

@router.get("/", response_model=List[CategoryRead])
def get_categories(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return CategoryService.get_all_categories(db)

@router.post("/", response_model=CategoryRead)
def create_category(
    payload: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return CategoryService.create_category(db, payload)

@router.get("/categories/export")
def export_categories(db: Session = Depends(get_db)):
    excel_file = CategoryService.export_categories(db)

    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=categories.xlsx"}
    )