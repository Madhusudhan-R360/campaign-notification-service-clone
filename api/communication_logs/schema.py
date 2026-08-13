from pydantic import BaseModel
from typing import Literal


class UpdateStatusSchema(BaseModel):

    status: Literal[
        "pending",
        "processing",
        "completed",
        "failed"
    ]