from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.config import get_db
from schemas.requests.template_request import TemplateCreateRequest, TemplateUpdateRequest
from schemas.responses.common_response import IdResponse
from schemas.responses.template_response import TemplateResponse

router = APIRouter()


@router.get("/{template_id}", description="템플릿 보기", response_model=TemplateResponse)
async def show_template(template_id: int, db: Session = Depends(get_db)) -> TemplateResponse:
    return TemplateResponse(id=template_id, user_id=1, snapshot=dict())


@router.post("", description="템플릿 작성", response_model=IdResponse, status_code=201)
async def write_template(
    template_request: TemplateCreateRequest, db: Session = Depends(get_db)
) -> IdResponse:
    return IdResponse(id=1)


@router.patch("/{template_id}", description="템플릿 수정", response_model=IdResponse)
async def update_template(
    template_id: int, template_request: TemplateUpdateRequest, db: Session = Depends(get_db)
) -> IdResponse:
    # TODO 수정이 똑같을 때는 202 raise
    return IdResponse(id=template_id)


@router.delete("/{template_id}", description="템플릿 삭제", response_model=IdResponse)
async def delete_template(template_id: int, db: Session = Depends(get_db)) -> IdResponse:
    # TODO 이미 삭제된 것은 204 raise
    return IdResponse(id=template_id)
