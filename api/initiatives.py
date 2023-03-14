from itertools import chain
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.initiative.create import create_initiative
from crud.initiative.delete import delete_initiative
from crud.initiative.update import done_initiative
from db.config import get_db
from db.models.initiative import Initiative
from db.models.user import User
from jwt import check_user
from schemas.requests.initiative_request import InitiativeCreateRequest
from validation.common import validate_id_in_objects

router = APIRouter()


# TODO done 과 initiative_id 위치 바꾸기
@router.post("/done/{initiative_id}", description="주요 행동 완료", response_model=None)
async def initiative_done(
    initiative_id: int,
    count: int = 1,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    user_initiatives: List[Initiative] = [
        kr.initiatives for kr in chain(*[obj.key_results for obj in user.objectives])
    ]
    validate_id_in_objects(list(chain(*user_initiatives)), initiative_id)

    await done_initiative(initiative_id, db, count)


@router.post("", description="주요 행동 만들기", response_model=int, status_code=201)
async def create_my_initiative(
    initiative_request: InitiativeCreateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> int:
    validate_id_in_objects(
        list(chain(*[obj.key_results for obj in user.objectives])),
        initiative_request.key_result_id,
    )

    return await create_initiative(initiative_request.make_initiative_schema(), db)


@router.delete("", description="주요 행동 삭제", response_model=None)
async def delete_my_initiative(
    initiative_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    user_initiatives: List[Initiative] = [
        kr.initiatives for kr in chain(*[obj.key_results for obj in user.objectives])
    ]
    validate_id_in_objects(list(chain(*user_initiatives)), initiative_id)

    await delete_initiative(initiative_id, db)
