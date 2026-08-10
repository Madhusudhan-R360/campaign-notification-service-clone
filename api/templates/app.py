from fastapi import APIRouter

from api.templates.schema import (
    CreateTemplateSchema
)

from api.templates import utility

router = APIRouter()


@router.post("/templates")
async def create_template(
    data: CreateTemplateSchema
):

    return await (
        utility.create_template(
            data.model_dump()
        )
    )


@router.get("/templates")
async def get_templates():

    return await (
        utility.get_templates()
    )


@router.get(
    "/templates/{template_id}"
)
async def get_template(
    template_id: str
):

    return await (
        utility.get_template(
            template_id
        )
    )