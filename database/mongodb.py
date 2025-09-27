from dotenv import load_dotenv

load_dotenv()
import motor.motor_asyncio
from pydantic import BaseSettings
import os

MONGODB_URL = os.environ.get("MONGODB_URL")

if not MONGODB_URL:
    raise KeyError("MONGODB_URL is not set")


class Settings(BaseSettings):
    mongodb_url: str = MONGODB_URL
    db_name: str = "citizen_service_db"


settings = Settings()

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client[settings.db_name]
