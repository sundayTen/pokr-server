from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends

from db.models.user import User
from jwt import check_user
from schemas.objective import ObjectiveWithKeyResultsSchema
from schemas.responses.okr_response import make_okr_response, OkrObjectiveResponse

router = APIRouter()


@router.get(
    "",
    description="OKR 전체 데이터 반환",
    response_model=list[OkrObjectiveResponse],
)
async def get_my_okr(
    user: User = Depends(check_user),
) -> List[ObjectiveWithKeyResultsSchema]:
    return await make_okr_response(user.objectives)


@router.get(
    "/years",
    description="가입 해부터 현재 해까지 반환",
)
async def get_my_okr(
    user: User = Depends(check_user),
) -> List[int]:
    return list(range(int(user.created_at.year), int(datetime.now().year) + 1))
