from fastapi import (
    APIRouter,
    BackgroundTasks
)

from api.notifications.schema import (
    NotificationSchema
)

from services.notification_processor import (
    process_notification
)

from api.notifications import utility

router = APIRouter()

@router.post("/notifications/send-otp")
async def send_otp(
    data: NotificationSchema,
    background_tasks: BackgroundTasks
):
    response = await utility.create_notification(
        data.model_dump()
    )

    background_tasks.add_task(
        process_notification,
        response["log_id"],
        data.recipient,
        data.channel
    )

    return response

@router.post("/notifications/campaign")
async def campaign_notification(
    data: NotificationSchema,
    background_tasks: BackgroundTasks
):
    response = await utility.create_notification(
        data.model_dump()
    )

    background_tasks.add_task(
        process_notification,
        response["log_id"],
        data.recipient,
        data.channel
    )

    return response

@router.post("/notifications/order")
async def order_notification(
    data: NotificationSchema,
    background_tasks: BackgroundTasks
):
    response = await utility.create_notification(
        data.model_dump()
    )

    background_tasks.add_task(
        process_notification,
        response["log_id"],
        data.recipient,
        data.channel
    )

    return response

@router.post("/notifications/reminder")
async def reminder_notification(
    data: NotificationSchema,
    background_tasks: BackgroundTasks
):
    response = await utility.create_notification(
        data.model_dump()
    )

    background_tasks.add_task(
        process_notification,
        response["log_id"],
        data.recipient,
        data.channel
    )

    return response

@router.get("/notifications")
async def get_notifications():

    return await utility.get_notifications()

@router.get(
    "/notifications/{notification_id}"
)
async def get_notification(
    notification_id: str
):

    return await utility.get_notification(
        notification_id
    )