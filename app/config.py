from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", extra="ignore")

    environment: Literal["development", "test", "production"] = "production"
    version: str = "0.1.0"
    greeting: str = "CI/CD pipeline is healthy"


@lru_cache
def get_settings() -> Settings:
    return Settings()
