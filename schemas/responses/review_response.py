from fastapi_camelcase import CamelModel


class ReviewResponse(CamelModel):
    id: int
    year: int
    quarter: int
    title: str
    content: str
