from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


@lru_cache()
def get_settings():
    settings = EnvSettings(_env_file=".env", _env_file_encoding="utf-8")
    return settings


class Settings(BaseSettings):
    APP_NAME: str = "Starter App"


class EnvSettings(Settings):
    MONGO_DB: str = Field(env="MONGO_DB", default="mongodb://localhost:27017")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


APP_SETTINGS = get_settings()
