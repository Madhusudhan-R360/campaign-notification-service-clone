from fastapi import APIRouter

from api.communication_logs.schema import (
    UpdateStatusSchema
)

from api.communication_logs import utility

router = APIRouter()


@router.get(
    "/communication-logs"
)
async def get_logs():

    return await utility.get_logs()


@router.get(
    "/communication-logs/{log_id}"
)
async def get_log(
    log_id: str
):

    return await utility.get_log(
        log_id
    )


@router.patch(
    "/communication-logs/{log_id}/status"
)
async def update_status(
    log_id: str,
    data: UpdateStatusSchema
):

    return await utility.update_status(
        log_id,
        data.status
    )