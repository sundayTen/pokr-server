from itertools import chain

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.initiative.create import create_initiative
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.requests.initiative_request import InitiativeCreateRequest
from validation.common import validate_id_in_objects

router = APIRouter()


@router.post("/done/{initiative_id}", description="주요 행동 완료", response_model=None)
async def initiative_done(
    initiative_id: int, db: Session = Depends(get_db), user: User = Depends(check_user)
) -> None:
    return


@router.post("/", description="주요 행동 만들기", response_model=int, status_code=201)
async def create_my_key_result(
    initiative_request: InitiativeCreateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> int:
    validate_id_in_objects(
        list(chain(*[obj.key_results for obj in user.objectives])),
        initiative_request.key_result_id,
    )

    return await create_initiative(initiative_request.make_initiative_schema(), db)
