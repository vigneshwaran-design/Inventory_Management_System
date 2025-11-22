from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schema.sales_schema import SaleCreate, SaleResponse
from ..services.sales_service import SalesService
from ..core.deps import get_current_user

router = APIRouter(prefix="/sales", tags=["Sales"],dependencies=[Depends(get_current_user)])

@router.post("/", response_model=SaleResponse)
def create_sale(data: SaleCreate, db: Session = Depends(get_db)):
    return SalesService.create_sale(db, data)

@router.get("/", response_model=list[SaleResponse])
def list_sales(db: Session = Depends(get_db)):
    return SalesService.get_all(db)

@router.get("/summary")
def sales_summary(db: Session = Depends(get_db)):
    return {"sales_chart": SalesService.get_summary(db)}

@router.get("/dashboard")
def sales_dashboard(db: Session = Depends(get_db)):
    return {
        "monthly_sales": SalesService.monthly_sales_chart(db),
        "last_7_days": SalesService.last_7_days_sales(db),
        "sales_by_category": SalesService.sales_by_category(db)
    }
