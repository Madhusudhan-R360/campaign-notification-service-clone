from fastapi import APIRouter

from api.notifications.schema import (
    NotificationSchema
)

from api.notifications import utility

router = APIRouter()

@router.post(
    "/notifications/send-otp"
)
async def send_otp(
    data: NotificationSchema
):

    return await utility.create_notification(
        data.model_dump()
    )

@router.post(
    "/notifications/campaign"
)
async def campaign_notification(
    data: NotificationSchema
):

    return await utility.create_notification(
        data.model_dump()
    )

@router.post(
    "/notifications/order"
)
async def order_notification(
    data: NotificationSchema
):

    return await utility.create_notification(
        data.model_dump()
    )

@router.post(
    "/notifications/reminder"
)
async def reminder_notification(
    data: NotificationSchema
):

    return await utility.create_notification(
        data.model_dump()
    )

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