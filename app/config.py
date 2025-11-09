import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET: str = os.getenv("JWT_SECRET", "mysecretkey")
    ALGORITHM: str = "HS256"
    ACCESS_EXPIRE_MINUTES: int = 15
    REFRESH_EXPIRE_DAYS: int = 7
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")

    class Config:
        env_file = ".env"

settings = Settings()