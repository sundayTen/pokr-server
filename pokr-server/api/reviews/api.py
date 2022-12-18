from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.review.create import create_review
from db.config import get_db
from schemas.requests.review_request import ReviewCreateRequest

router = APIRouter()


@router.post("", description="리뷰 작성", response_model=dict)
async def signup(
    review_request: ReviewCreateRequest, db: Session = Depends(get_db)
) -> dict:
    # TODO 현재는 유저가 하나라도 있어야 가능, JWT 기능 필요.
    review_id: int = await create_review(1, review_request.make_review_schema(), db)

    return {"id": review_id}
