from typing import List

from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from sqlalchemy.orm import Session

from crud.objective.create import create_objective, copy_objective
from crud.objective.delete import delete_objective
from crud.objective.update import update_objective
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.requests.objective_request import (
    ObjectiveCreateRequest,
    ObjectiveUpdateRequest,
)
from schemas.responses.common_response import IdResponse
from schemas.responses.objective_response import (
    ObjectiveResponse,
    make_objective_response,
)
from validation.common import validate_id_in_objects

router = APIRouter()


@router.get("/", description="년도별 나의 모든 목표 보기")
async def get_my_goals(
    year: int = Query(ge=2023), user: User = Depends(check_user)
) -> List[ObjectiveResponse]:
    objectives = list(filter(lambda x: x.year == year, user.objectives))
    return [await make_objective_response(objective) for objective in objectives]


@router.get("/{objective_id}", description="목표 상세 정보")
async def get_my_goal(
    objective_id: int,
    user: User = Depends(check_user),
) -> ObjectiveResponse:
    objectives = list(filter(lambda x: x.id == objective_id, user.objectives))
    if not objectives:
        raise HTTPException(status_code=404, detail="Wrong Objective Id")

    return await make_objective_response(objectives[0])


@router.post("", description="목표 만들기", status_code=201)
async def create_my_goal(
    objective_request: ObjectiveCreateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> IdResponse:
    return IdResponse(
        id=await create_objective(
            user.id, objective_request.make_objective_schema(), db
        )
    )


@router.delete("/{objective_id}", description="목표 삭제")
async def delete_my_goal(
    objective_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    await validate_id_in_objects(user.objectives, objective_id)

    await delete_objective(objective_id, db)


@router.patch("/{objective_id}", description="목표 수정")
async def update_my_goal(
    objective_id: int,
    objective_request: ObjectiveUpdateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    await validate_id_in_objects(user.objectives, objective_id)

    await update_objective(
        objective_id, objective_request.make_objective_nullable_schema(), db
    )


@router.post("/{objective_id}/copy", description="목표 복제")
async def copy_my_goal(
    objective_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> IdResponse:
    await validate_id_in_objects(user.objectives, objective_id)

    return IdResponse(
        id=await copy_objective(
            next(filter(lambda x: x.id == objective_id, user.objectives)), db
        )
    )
