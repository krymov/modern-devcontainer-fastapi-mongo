from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configuration settings for the Starter App.

    Attributes
    ----------
        APP_NAME (str): The name of the application.

    """

    APP_NAME: str = "Starter App"


class EnvSettings(Settings):
    """Configuration settings for the application environment.

    Attributes
    ----------
        MONGO_DB (str): The MongoDB connection string. Defaults to "mongodb://localhost:27017".

    Config:
        env_file (str): The path to the environment file. Defaults to ".env".
        env_file_encoding (str): The encoding of the environment file.
        Defaults to "utf-8".

    """

    MONGO_DB: str = Field(env="MONGO_DB", default="mongodb://localhost:27017")

    class Config:
        """Configuration class for the application.

        Attributes
        ----------
            env_file (str): The path to the environment file.
            env_file_encoding (str): The encoding of the environment file.

        """

        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> EnvSettings:
    """Get the application settings.

    Returns
    -------
        EnvSettings: The application settings.

    """
    return EnvSettings(_env_file=".env", _env_file_encoding="utf-8")


APP_SETTINGS = get_settings()
