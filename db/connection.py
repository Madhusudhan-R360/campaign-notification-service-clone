import motor.motor_asyncio

from db.config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.mongo_url
)

db = client[
    settings.database_name
]