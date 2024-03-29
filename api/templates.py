from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.config import get_db
from schemas.requests.template_request import (
    TemplateCreateRequest,
    TemplateUpdateRequest,
)
from schemas.responses.common_response import IdResponse
from schemas.responses.template_response import TemplateResponse

router = APIRouter()


@router.get("/{template_id}", description="템플릿 보기")
async def show_template(
    template_id: int, db: Session = Depends(get_db)
) -> TemplateResponse:
    return TemplateResponse(id=template_id, user_id=1, snapshot=dict())


@router.post("", description="템플릿 작성", status_code=201)
async def write_template(
    template_request: TemplateCreateRequest, db: Session = Depends(get_db)
) -> IdResponse:
    return IdResponse(id=1)


@router.patch("/{template_id}", description="템플릿 수정")
async def update_template(
    template_id: int,
    template_request: TemplateUpdateRequest,
    db: Session = Depends(get_db),
) -> IdResponse:
    return IdResponse(id=template_id)


@router.delete("/{template_id}", description="템플릿 삭제")
async def delete_template(
    template_id: int, db: Session = Depends(get_db)
) -> IdResponse:
    return IdResponse(id=template_id)
