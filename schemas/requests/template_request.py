from pydantic import BaseModel


class TemplateCreateRequest(BaseModel):
    snapshot: dict


class TemplateUpdateRequest(BaseModel):
    snapshot: dict
