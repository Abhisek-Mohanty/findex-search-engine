import logging
import sys
from typing import List

from databases import DatabaseURL
from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret
from fastapi.encoders import jsonable_encoder


URL_PREFIX = "/api/v1"
API_PREFIX = "/api/v2"
WS_PREFIX  = "/ws/v1"
WEBHOOK_PREFIX  = "/webhook/v1"

JWT_TOKEN_PREFIX = "Bearer"

config = Config(".env")

SUPABASE_USERNAME: str = config("SUPABASE_USERNAME", cast=str, default="1.0.0")
PASSWORD: str = config("PASSWORD", cast=str, default="1.0.0")

