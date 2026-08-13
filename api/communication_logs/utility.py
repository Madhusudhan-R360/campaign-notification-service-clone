from bson import ObjectId

from db.connection import (
    communication_logs_collection
)


async def get_logs():

    logs = await (
        communication_logs_collection
        .find()
        .to_list(None)
    )

    for log in logs:

        log["_id"] = str(log["_id"])

        if "notification_id" in log:
            log["notification_id"] = str(
                log["notification_id"]
            )
    
    return logs


async def get_log(
    log_id: str
):

    log = await (
        communication_logs_collection
        .find_one(
            {
                "_id": ObjectId(log_id)
            }
        )
    )

    if not log:
        return {
            "success": False,
            "message": "Log not found"
        }

    log["_id"] = str(log["_id"])

    if "notification_id" in log:
        log["notification_id"] = str(
        log["notification_id"]
    )

    return log


async def update_status(
    log_id: str,
    status: str
):

    result = await (
        communication_logs_collection
        .update_one(
            {
                "_id": ObjectId(log_id)
            },
            {
                "$set": {
                    "status": status
                }
            }
        )
    )

    if result.modified_count == 0:

        return {
            "success": False,
            "message": "Log not found"
        }

    return {
        "success": True,
        "message": "Status updated"
    }