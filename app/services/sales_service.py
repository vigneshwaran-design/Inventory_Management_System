from sqlalchemy.orm import Session
from ..models.sales_model import Sale
from ..models.product_model import Product
from ..schema.sales_schema import SaleCreate
from ..models.category_model import Category
from ..models.product_model import Product
    
from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy import extract
from datetime import datetime, timedelta


class SalesService:

    @staticmethod
    def create_sale(db: Session, data: SaleCreate):
        product = db.query(Product).filter(Product.id == data.product_id).first()
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")

        if product.quantity < data.quantity:
            raise HTTPException(status_code=400, detail="Insufficient stock")

        # Update stock
        product.quantity -= data.quantity

        # Calculate price
        total_price = product.price * data.quantity

        sale = Sale(
            product_id=data.product_id,
            quantity=data.quantity,
            total_price=total_price,
        )

        db.add(sale)
        db.commit()
        db.refresh(sale)

        return sale

    @staticmethod
    def get_all(db: Session):
        return db.query(Sale).order_by(Sale.id.desc()).all()

    @staticmethod
    def get_summary(db: Session):
        """Group sales by month for dashboard charts"""
        from sqlalchemy import extract

        results = (
            db.query(
                extract('month', Sale.created_at).label("month"),
                func.sum(Sale.total_price).label("total_sales"),
            )
            .group_by(extract('month', Sale.created_at))
            .all()
        )

        return [
            {"month": int(month), "sales": float(total_sales)}
            for month, total_sales in results
        ]
 
    def monthly_sales_chart(db: Session):

        rows = (
            db.query(
                extract('month', Sale.created_at).label("month"),
                func.sum(Sale.total_price).label("total_sales")
            )
            .group_by(extract('month', Sale.created_at))
            .order_by(extract('month', Sale.created_at))
            .all()
        )

        return [
            {"month": int(month), "sales": float(total_sales)}
            for month, total_sales in rows
        ]
    
    def last_7_days_sales(db: Session):
 
        seven_days_ago = datetime.utcnow() - timedelta(days=7)

        rows = (
            db.query(
                func.date(Sale.created_at).label("date"),
                func.sum(Sale.total_price)
            )
            .filter(Sale.created_at >= seven_days_ago)
            .group_by(func.date(Sale.created_at))
            .all()
        )

        return [
            {"date": str(date), "sales": float(total_sales)}
            for date, total_sales in rows
        ]
        
    def sales_by_category(db: Session):
   

        rows = (
            db.query(Category.name, func.sum(Sale.total_price))
            .join(Product, Product.category_id == Category.id)
            .join(Sale, Sale.product_id == Product.id)
            .group_by(Category.name)
            .all()
        )

        return [
            {"name": name, "value": float(total_sales)}
            for name, total_sales in rows
        ]