from sqlalchemy.orm import Session

from schemas.review import ReviewSchema


async def create_review(user_id: int, review_schema: ReviewSchema, db: Session) -> int:
    review = review_schema.make_review(user_id)
    db.add(review)
    db.commit()

    return review.id
