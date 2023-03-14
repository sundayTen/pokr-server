from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from crud.objective.create import create_objective
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.requests.objective_request import ObjectiveCreateRequest

router = APIRouter()


@router.post("", description="목표 만들기", response_model=int, status_code=201)
async def create_my_goal(
    objective_request: ObjectiveCreateRequest,
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> int:
    return await create_objective(
        user.id, objective_request.make_objective_schema(), db
    )
