import sys
import os

# Add project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import Base, engine

from app.models.user_model import User
from app.models.product_model import Product
from app.models.category_model import Category
from app.models.supplier_model import Supplier
from app.models.sales_model import Sale

def init_db():
    print("🔄 Creating tables in database...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")

if __name__ == "__main__":
    init_db()
