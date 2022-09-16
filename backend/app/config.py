import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl

log = logging.getLogger("uvicorn")

class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")
    jwt_secret: str = os.environ.get("SECRET_KEY")
    jwt_algorithm: str =  os.environ.get("ALGORITHM")
    token_expires: int = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES ")

@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()