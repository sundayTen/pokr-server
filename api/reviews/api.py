from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.review.create import create_review
from db.config import get_db
from schemas.requests.review_request import ReviewCreateRequest, ReviewUpdateRequest
from schemas.responses.common_response import IdResponse
from schemas.responses.review_response import ReviewResponse

router = APIRouter()


@router.get("/{review_id}", description="회고 읽기", response_model=ReviewResponse)
async def read_review(review_id: int, db: Session = Depends(get_db)) -> ReviewResponse:
    return ReviewResponse(
        id=review_id, year=2023, quarter=1, title="안녕하세요", content="더미데이터입니다."
    )


@router.post("", description="회고 작성", response_model=IdResponse, status_code=201)
async def post_review(
    review_request: ReviewCreateRequest, db: Session = Depends(get_db)
) -> IdResponse:
    # TODO 현재는 유저가 하나라도 있어야 가능, JWT 기능 필요.
    review_id: int = await create_review(1, review_request.make_review_schema(), db)

    return IdResponse(id=review_id)


@router.patch("/{review_id}", description="회고 수정", response_model=IdResponse)
async def update_review(
    review_id: int, review_request: ReviewUpdateRequest, db: Session = Depends(get_db)
) -> IdResponse:
    # TODO 수정이 똑같을 때는 202 raise
    return IdResponse(id=review_id)


@router.delete("/{review_id}", description="회고 삭제", response_model=IdResponse)
async def delete_review(review_id: int, db: Session = Depends(get_db)) -> IdResponse:
    # TODO 이미 삭제된 것은 204 raise
    return IdResponse(id=review_id)
