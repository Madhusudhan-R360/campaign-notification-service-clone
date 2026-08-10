from fastapi import FastAPI

app = FastAPI(
    title="Campaign Notification Service Clone"
)

from api.templates.app import (
    router as templates_router
)

app.include_router(
    templates_router
)

@app.get("/health")
async def health():

    return {
        "success": True
    }