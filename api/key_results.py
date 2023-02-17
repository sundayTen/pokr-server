from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.key_result.create import create_key_result
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.requests.key_result_request import KeyResultCreateRequest
from validation.common import validate_id_in_objects

router = APIRouter()


@router.post("/", description="핵심 지표 만들기", response_model=int, status_code=201)
async def create_my_key_result(
    key_result_request: KeyResultCreateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> int:
    validate_id_in_objects(user.objectives, key_result_request.objective_id)

    return await create_key_result(key_result_request.make_key_result_schema(), db)
