from pydantic import BaseModel


class TemplateResponse(BaseModel):
    id: int
    user_id: int
    snapshot: dict
