import motor.motor_asyncio
from pydantic import BaseSettings


class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    db_name: str = "citizen_service_db"  


settings = Settings()

client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
db = client[settings.db_name]
