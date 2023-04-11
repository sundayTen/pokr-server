from fastapi_camelcase import CamelModel


class IdResponse(CamelModel):
    id: int


class TokenResponse(CamelModel):
    access_token: str
    token_type: str
