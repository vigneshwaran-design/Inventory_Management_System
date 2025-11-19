from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schema import CategoryCreate, CategoryUpdate, CategoryResponse
from app.services import CategoryService

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.post("/", response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)):
    return CategoryService.create(db, data)

@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return CategoryService.get_all(db)

@router.put("/{id}", response_model=CategoryResponse)
def update_category(id: int, data: CategoryUpdate, db: Session = Depends(get_db)):
    return CategoryService.update(db, id, data)
