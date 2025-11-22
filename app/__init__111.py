from fastapi import FastAPI
from .routes import auth, products, categories, suppliers

app = FastAPI(title="Inventory Management System")

# Register Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth111"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(suppliers.router, prefix="/suppliers", tags=["Suppliers"])
