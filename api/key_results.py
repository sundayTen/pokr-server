from itertools import chain

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.key_result.create import create_key_result
from crud.key_result.delete import delete_key_result
from crud.key_result.update import update_key_result
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.requests.key_result_request import (
    KeyResultCreateRequest,
    KeyResultUpdateRequest,
)
from schemas.responses.common_response import IdResponse
from schemas.responses.key_result_response import (
    KeyResultResponse,
    make_key_result_response,
)
from validation.common import validate_id_in_objects, validate_period

router = APIRouter()


@router.get("/{key_result_id}", description="핵심 지표 상세 정보")
async def get_my_key_result(
    key_result_id: int,
    user: User = Depends(check_user),
) -> KeyResultResponse:
    key_results = list(
        filter(
            lambda x: x.id == key_result_id,
            list(chain(*[obj.key_results for obj in user.objectives])),
        )
    )
    if not key_results:
        raise HTTPException(status_code=404, detail="Wrong Key Result Id")

    return await make_key_result_response(key_results[0])


@router.post("", description="핵심 지표 만들기", status_code=201)
async def create_my_key_result(
    key_result_request: KeyResultCreateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> IdResponse:
    await validate_id_in_objects(user.objectives, key_result_request.objective_id)
    await validate_period(key_result_request.open_date, key_result_request.due_date)

    return IdResponse(
        id=await create_key_result(key_result_request.make_key_result_schema(), db)
    )


@router.delete("/{key_result_id}", description="핵심 지표 삭제")
async def delete_my_key_result(
    key_result_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    await validate_id_in_objects(
        chain(*[obj.key_results for obj in user.objectives]), key_result_id
    )

    await delete_key_result(key_result_id, db)


@router.patch("/{key_result_id}", description="핵심 지표 수정")
async def update_my_key_result(
    key_result_id: int,
    key_result_request: KeyResultUpdateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    key_result_generator = chain(*[obj.key_results for obj in user.objectives])
    await validate_id_in_objects(list(key_result_generator), key_result_id)
    for key_result in key_result_generator:
        if key_result.id == key_result_id:
            updatable_key_result = key_result

    await validate_period(
        key_result_request.open_date or updatable_key_result.open_date,
        key_result_request.due_date or updatable_key_result.due_date,
    )

    await update_key_result(
        key_result_id, key_result_request.make_key_result_nullable_schema(), db
    )
