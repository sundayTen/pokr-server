from fastapi_camelcase import CamelModel


class IdResponse(CamelModel):
    id: int
