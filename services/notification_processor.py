from bson import ObjectId

from db.connection import (
    communication_logs_collection
)

from services.email_service import (
    send_email
)

from services.sms_service import (
    send_sms
)


async def process_notification(
    log_id: str,
    recipient: str,
    channel: str
):

    await communication_logs_collection.update_one(
        {
            "_id": ObjectId(log_id)
        },
        {
            "$set": {
                "status": "processing"
            }
        }
    )

    success = False

    if channel == "email":

        success = await send_email(
            recipient
        )

    elif channel == "sms":

        success = await send_sms(
            recipient
        )

    await communication_logs_collection.update_one(
        {
            "_id": ObjectId(log_id)
        },
        {
            "$set": {
                "status": (
                    "completed"
                    if success
                    else "failed"
                )
            }
        }
    )
print("PROCESSING STARTED")