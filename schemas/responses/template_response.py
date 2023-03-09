from fastapi_camelcase import CamelModel


class TemplateResponse(CamelModel):
    id: int
    user_id: int
    snapshot: dict
