from pydantic import BaseModel


class ReviewResponse(BaseModel):
    id: int
    year: int
    quarter: int
    title: str
    content: str
