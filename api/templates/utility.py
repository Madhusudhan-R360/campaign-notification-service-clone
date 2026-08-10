from bson import ObjectId

from db.connection import (
    notification_templates_collection
)


async def create_template(data):

    result = await (
        notification_templates_collection
        .insert_one(data)
    )

    return {
        "success": True,
        "template_id": str(
            result.inserted_id
        )
    }


async def get_templates():

    templates = await (
        notification_templates_collection
        .find()
        .to_list(None)
    )

    for template in templates:
        template["_id"] = (
            str(template["_id"])
        )

    return templates


async def get_template(
    template_id: str
):

    template = await (
        notification_templates_collection
        .find_one(
            {
                "_id": ObjectId(
                    template_id
                )
            }
        )
    )

    if not template:

        return {
            "success": False,
            "message": "Template not found"
        }

    template["_id"] = str(
        template["_id"]
    )

    return template