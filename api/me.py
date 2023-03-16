from typing import List

from fastapi import APIRouter, Depends

from api.me_api.metrics import router as metrics_router
from db.models.user import User
from jwt import check_user
from schemas.objective import ObjectiveWithKeyResultsSchema
from schemas.responses.okr_response import make_okr_response, OkrObjectiveResponse

router = APIRouter()
router.routes.extend(metrics_router.routes)


@router.get(
    "/okr",
    description="OKR 전체 데이터 반환",
    response_model=list[OkrObjectiveResponse],
)
async def get_my_okr(
    user: User = Depends(check_user),
) -> List[ObjectiveWithKeyResultsSchema]:
    return make_okr_response(user.objectives)
