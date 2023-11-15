from starlette.testclient import TestClient
from app.main import create_application
from app.config import get_settings, Settings
from tortoise.contrib.fastapi import register_tortoise
