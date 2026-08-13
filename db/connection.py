import motor.motor_asyncio

from db.config import settings


client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.mongo_url
)

db = client[
    settings.database_name
]

notification_templates_collection = db[
    "notification_templates"
]

notifications_collection = db[
    "notifications"
]

communication_logs_collection = db[
    "communication_logs"
]