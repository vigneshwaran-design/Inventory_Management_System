from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .routes import auth, products, categories, suppliers,sales
from .config import settings

app = FastAPI(title="Inventory Management System")

# Serve Static Files
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Jinja Templates
templates = Jinja2Templates(directory="app/templates")



# Routers
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(categories.router, prefix="/categories", tags=["Categories"])
app.include_router(suppliers.router, prefix="/suppliers", tags=["Suppliers"])
app.include_router(sales.router)

@app.get("/")
def dashboard():
    return {"message": "Inventory API Running"}
