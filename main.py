from fastapi import FastAPI

from api.notifications.app import (
    router as notification_router
)

app = FastAPI(
    title="Campaign Notification Service Clone"
)

from api.templates.app import (
    router as templates_router
)

app.include_router(
    templates_router
)

app.include_router(
    notification_router
)

@app.get("/health")
async def health():

    return {
        "success": True
    }