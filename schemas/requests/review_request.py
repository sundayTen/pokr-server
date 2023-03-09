from fastapi_camelcase import CamelModel

from schemas.review import ReviewSchema


class ReviewCreateRequest(CamelModel):
    year: int
    quarter: int
    title: str
    content: str

    def make_review_schema(self):
        return ReviewSchema(
            year=self.year, quarter=self.quarter, title=self.title, content=self.content
        )


class ReviewUpdateRequest(CamelModel):
    year: int | None
    quarter: int | None
    title: str | None
    content: str | None
