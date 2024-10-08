"""
- You can define and manage configurations to use in your project.
    - `BaseSettings` in `pydantic_settings` can set config values based on system environment variables.
    - To use the Upstage Solar API, you need to put `API_KEY` as a system environment variable.
"""
import logging
from typing import Dict, Any

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    ENV: str = "local"
    TITLE: str = "Solar FastAPI Example"
    VERSION: str = "0.1.0"
    APP_HOST: str = "http://localhost:8080"
    OPENAPI_URL: str = "/openapi.json"
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"

    LOG_LEVEL: int = logging.INFO

    API_KEY: str

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "title": self.TITLE,
            "version": self.VERSION,
            "servers": [
                {"url": self.APP_HOST, "description": self.ENV}
            ],
            "openapi_url": self.OPENAPI_URL,
            "docs_url": self.DOCS_URL,
            "redoc_url": self.REDOC_URL,
        }

config: Config = Config()
