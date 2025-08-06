"""
Configuration for EPO OPS MCP Server
"""
import os
from typing import Optional
# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # EPO OPS credentials
    EPO_OPS_KEY: str = os.getenv("EPO_OPS_KEY", "")
    EPO_OPS_SECRET: str = os.getenv("EPO_OPS_SECRET", "")
    
    # Server settings
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    
    # Cache settings
    CACHE_ENABLED: bool = False
    CACHE_PATH: str = "/var/tmp/epo-ops-server/cache.dbm"
    
    class Config:
        env_file = ".env.epo"
        env_file_encoding = "utf-8"


settings = Settings()