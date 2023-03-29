from datetime import datetime, date
from typing import List

from fastapi import APIRouter, Depends

from db.models.user import User
from errors import WRONG_PARAMETER_EXCEPTION
from jwt import check_user
from schemas.objective import ObjectiveWithKeyResultsSchema
from schemas.responses.okr_response import (
    make_okr_response,
    OkrObjectiveResponse,
)
from service.okr import filter_okr

router = APIRouter()


@router.get(
    "",
    description="기간에 맞는 OKR 전체 데이터 반환",
    response_model=list[OkrObjectiveResponse],
)
async def get_my_okr(
    start_date: date = date.min,
    end_date: date = date.max,
    user: User = Depends(check_user),
) -> List[ObjectiveWithKeyResultsSchema]:
    if start_date > end_date:
        raise WRONG_PARAMETER_EXCEPTION
    okrs = await make_okr_response(user.objectives)

    return await filter_okr(start_date, end_date, okrs)


@router.get(
    "/years",
    description="가입 해부터 현재 해까지 반환",
)
async def get_my_okr(
    user: User = Depends(check_user),
) -> List[int]:
    return list(range(int(user.created_at.year), int(datetime.now().year) + 1))
