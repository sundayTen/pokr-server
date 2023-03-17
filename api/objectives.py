from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from crud.objective.create import create_objective
from crud.objective.delete import delete_objective
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.requests.objective_request import ObjectiveCreateRequest
from schemas.responses.objective_response import (
    ObjectiveResponse,
    make_objective_response,
)
from validation.common import validate_id_in_objects

router = APIRouter()


@router.get("/{objective_id}", description="목표 상세 정보")
async def create_my_goal(
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
) -> int:
    return await create_objective(
        user.id, objective_request.make_objective_schema(), db
    )


@router.delete("", description="목표 삭제")
async def delete_my_goal(
    objective_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> None:
    validate_id_in_objects(user.objectives, objective_id)

    await delete_objective(objective_id, db)
