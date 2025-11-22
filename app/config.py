from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me-please")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    ALGORITHM: str = "HS256"
    PROJECT_NAME: str = "Inventory Management"
    TEMPLATE_DIR: str = "templates"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
