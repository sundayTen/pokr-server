from itertools import chain
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.initiative.create import create_initiative
from crud.initiative.delete import delete_initiative
from crud.initiative.update import done_initiative, update_initiative
from db.config import get_db
from db.models.initiative import Initiative
from db.models.user import User
from jwt import check_user
from schemas.requests.initiative_request import (
    InitiativeCreateRequest,
    InitiativeUpdateRequest,
)
from schemas.responses.common_response import IdResponse
from schemas.responses.initiative_response import (
    make_initiative_response,
    InitiativeResponse,
)
from validation.common import validate_id_in_objects

router = APIRouter()


@router.get("/{initiative_id}", description="주요 행동 상세 정보")
async def get_my_initiative(
    initiative_id: int,
    user: User = Depends(check_user),
) -> InitiativeResponse:
    user_initiatives: List[List[Initiative]] = [
        kr.initiatives for kr in chain(*[obj.key_results for obj in user.objectives])
    ]
    initiatives = list(
        filter(lambda x: x.id == initiative_id, chain(*user_initiatives))
    )
    if not initiatives:
        raise HTTPException(status_code=404, detail="Wrong Initiative Id")

    return await make_initiative_response(initiatives[0])


@router.post("", description="주요 행동 만들기", status_code=201)
async def create_my_initiative(
    initiative_request: InitiativeCreateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> IdResponse:
    await validate_id_in_objects(
        list(chain(*[obj.key_results for obj in user.objectives])),
        initiative_request.key_result_id,
    )

    return IdResponse(
        id=await create_initiative(initiative_request.make_initiative_schema(), db)
    )


@router.delete("/{initiative_id}", description="주요 행동 삭제")
async def delete_my_initiative(
    initiative_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    user_initiatives: List[List[Initiative]] = [
        kr.initiatives for kr in chain(*[obj.key_results for obj in user.objectives])
    ]
    await validate_id_in_objects(list(chain(*user_initiatives)), initiative_id)

    await delete_initiative(initiative_id, db)


@router.patch("/{initiative_id}", description="주요 행동 수정")
async def update_my_initiative(
    initiative_id: int,
    initiative_request: InitiativeUpdateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    user_initiatives: List[List[Initiative]] = [
        kr.initiatives for kr in chain(*[obj.key_results for obj in user.objectives])
    ]
    await validate_id_in_objects(list(chain(*user_initiatives)), initiative_id)

    await update_initiative(
        initiative_id, initiative_request.make_initiative_nullable_schema(), db
    )


@router.post("/{initiative_id}/done", description="주요 행동 완료")
async def check_done_initiative(
    initiative_id: int,
    count: int = 1,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    user_initiatives: List[List[Initiative]] = [
        kr.initiatives for kr in chain(*[obj.key_results for obj in user.objectives])
    ]
    await validate_id_in_objects(list(chain(*user_initiatives)), initiative_id)

    await done_initiative(initiative_id, db, count)
