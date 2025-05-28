from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/heroku_hackathon"
    )
    # Ensure SQLAlchemy compatibility with Heroku's DATABASE_URL
    if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)
    print("DEBUG: DATABASE_URL used:", DATABASE_URL)

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
