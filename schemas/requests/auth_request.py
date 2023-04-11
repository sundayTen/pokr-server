from fastapi_camelcase import CamelModel


class NaverSignupRequest(CamelModel):
    access_token: str
