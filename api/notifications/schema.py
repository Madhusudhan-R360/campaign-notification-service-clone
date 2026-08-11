from pydantic import BaseModel
from typing import Literal


class NotificationSchema(BaseModel):

    recipient: str

    channel: Literal[
        "email",
        "sms"
    ]

    notification_type: Literal[
        "otp",
        "campaign",
        "order",
        "reminder"
    ]

    payload: dict