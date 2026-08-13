from bson import ObjectId

from db.connection import (
    notifications_collection, communication_logs_collection
)

async def create_notification(data):

    data["status"] = "pending"

    result = await notifications_collection.insert_one(
        data
    )

    log_result = await (
        communication_logs_collection.insert_one(
            {
                "notification_id": str(
                    result.inserted_id
                ),
                "channel": data["channel"],
                "notification_type": data[
                    "notification_type"
                ],
                "status": "pending"
            }
        )
    )

    return {
        "success": True,
        "notification_id": str(
            result.inserted_id
        ),
        "log_id": str(
            log_result.inserted_id
        )
    }

async def get_notifications():

    notifications = await (
        notifications_collection
        .find()
        .to_list(None)
    )

    for notification in notifications:

        notification["_id"] = str(
            notification["_id"]
        )

    return notifications


async def get_notification(
    notification_id: str
):

    notification = await (
        notifications_collection
        .find_one(
            {
                "_id": ObjectId(
                    notification_id
                )
            }
        )
    )

    if not notification:

        return {
            "success": False,
            "message": "Notification not found"
        }

    notification["_id"] = str(
        notification["_id"]
    )

    return notification