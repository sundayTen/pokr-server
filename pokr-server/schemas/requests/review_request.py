from pydantic import BaseModel

from schemas.review import ReviewSchema


class ReviewCreateRequest(BaseModel):
    year: int
    quarter: int
    title: str
    content: str

    def make_review_schema(self):
        return ReviewSchema(
            year=self.year, quarter=self.quarter, title=self.title, content=self.content
        )
