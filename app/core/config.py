from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI API Server"
    DATABASE_URL: str
    REDIS_URL: str
    SECRET_KEY: str
    API_KEY: str
    GOOGLE_CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str
    MAGIC_LINK_SECRET: str
    CORS_ORIGINS: List[str] = ["http://localhost:3000"]
    ELL_AI_API_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()