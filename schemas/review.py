from fastapi_camelcase import CamelModel

from db.models.review import Review


class ReviewSchema(CamelModel):
    year: int
    quarter: int
    title: str
    content: str

    def make_review(self, user_id: int) -> Review:
        return Review(
            user_id=user_id,
            year=self.year,
            quarter=self.quarter,
            title=self.title,
            content=self.content,
        )
