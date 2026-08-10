from pydantic import BaseModel


class CreateTemplateSchema(BaseModel):

    template_name: str

    subject: str

    content: str