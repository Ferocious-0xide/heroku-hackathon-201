from pydantic_settings import BaseSettings
from functools import lru_cache
import os

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:postgres@localhost:5432/heroku_hackathon"
    )
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Ensure SQLAlchemy compatibility with Heroku's DATABASE_URL
        if self.DATABASE_URL and self.DATABASE_URL.startswith("postgres://"):
            self.DATABASE_URL = self.DATABASE_URL.replace("postgres://", "postgresql://", 1)
        print("DEBUG: DATABASE_URL used:", self.DATABASE_URL)

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()
