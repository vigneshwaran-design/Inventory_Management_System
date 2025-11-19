from fastapi import FastAPI
from app.database import engine, Base
from app.routes import product_router, category_router, supplier_router

app = FastAPI(title="Inventory Management")

# create tables on startup (for simple deployments)
Base.metadata.create_all(bind=engine)

# include routers
app.include_router(product_router)
app.include_router(category_router)
app.include_router(supplier_router)

@app.get("/")
def root():
    return {"status": "ok"}
