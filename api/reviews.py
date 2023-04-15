from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.review.create import create_review
from db.config import get_db
from schemas.requests.review_request import ReviewCreateRequest, ReviewUpdateRequest
from schemas.responses.common_response import IdResponse
from schemas.responses.review_response import ReviewResponse

router = APIRouter()


@router.get("/{review_id}", description="회고 읽기")
async def read_review(review_id: int, db: Session = Depends(get_db)) -> ReviewResponse:
    return ReviewResponse(
        id=review_id, year=2023, quarter=1, title="안녕하세요", content="더미데이터입니다."
    )


@router.post("", description="회고 작성", status_code=201)
async def post_review(
    review_request: ReviewCreateRequest, db: Session = Depends(get_db)
) -> IdResponse:
    review_id: int = await create_review(1, review_request.make_review_schema(), db)

    return IdResponse(id=review_id)


@router.patch("/{review_id}", description="회고 수정")
async def update_review(
    review_id: int, review_request: ReviewUpdateRequest, db: Session = Depends(get_db)
) -> IdResponse:
    return IdResponse(id=review_id)


@router.delete("/{review_id}", description="회고 삭제")
async def delete_review(review_id: int, db: Session = Depends(get_db)) -> IdResponse:
    return IdResponse(id=review_id)
