from fastapi import FastAPI

app = FastAPI(
    title="Campaign Notification Service Clone"
)


@app.get("/health")
async def health():

    return {
        "success": True
    }