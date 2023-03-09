from typing import List

from fastapi import APIRouter, Depends

from api.me_api.metrics import router as metrics_router
from db.models.user import User
from jwt import check_user
from schemas.objective import ObjectiveWithKeyResultsSchema
from schemas.responses.okr_response import make_okr_response

router = APIRouter()
router.routes.extend(metrics_router.routes)


# TODO api 문서가 제대로 적용이 안 됨.
@router.get(
    "/okr",
    description="OKR 전체 데이터 반환",
    response_model=list[dict],
)
async def get_my_okr(
    user: User = Depends(check_user),
) -> List[ObjectiveWithKeyResultsSchema]:
    return make_okr_response(user.objectives)
