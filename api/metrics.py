from typing import List

from fastapi import Depends, Path, APIRouter
from sqlalchemy.orm import Session

from db.config import get_db
from db.models.user import User
from jwt import check_user

router = APIRouter()


@router.get("/graph/half/{num}", description="나의 달성 수치[월별]", response_model=List[dict])
async def get_my_monthly_metrics(
    num: int = Path(..., ge=1, le=2),
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> List[dict]:
    if num == 1:
        return [
            {"label": "1월", "me_api": 14, "all": 20},
            {"label": "2월", "me_api": 45, "all": 40},
            {"label": "3월", "me_api": 75, "all": 60},
            {"label": "4월", "me_api": 50, "all": 50},
            {"label": "5월", "me_api": 84, "all": 66},
            {"label": "6월", "me_api": 90, "all": 44},
        ]
    else:
        return [
            {"label": "7월", "me_api": 100, "all": 33},
            {"label": "8월", "me_api": 82, "all": 46},
            {"label": "9월", "me_api": 47, "all": 23},
            {"label": "10월", "me_api": 90, "all": 49},
            {"label": "11월", "me_api": 77, "all": 80},
            {"label": "12월", "me_api": 100, "all": 70},
        ]


@router.get(
    "/graph/quarter/{num}",
    description="나의 달성 수치[주별]",
    response_model=List[dict],
)
async def get_my_weekly_metrics(
    num: int = Path(..., ge=1, le=4),
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> List[dict]:
    if num == 1:
        return [
            {"label": "1월 1주차", "me_api": 14, "all": 20},
            {"label": "1월 2주차", "me_api": 45, "all": 40},
            {"label": "1월 3주차", "me_api": 75, "all": 60},
            {"label": "1월 4주차", "me_api": 50, "all": 50},
            {"label": "1월 5주차", "me_api": 84, "all": 66},
            {"label": "2월 1주차", "me_api": 90, "all": 44},
            {"label": "2월 2주차", "me_api": 100, "all": 33},
            {"label": "2월 3주차", "me_api": 82, "all": 46},
            {"label": "2월 4주차", "me_api": 47, "all": 23},
            {"label": "3월 1주차", "me_api": 90, "all": 49},
            {"label": "3월 2주차", "me_api": 77, "all": 80},
            {"label": "3월 3주차", "me_api": 100, "all": 70},
            {"label": "3월 4주차", "me_api": 71, "all": 90},
            {"label": "3월 5주차", "me_api": 50, "all": 70},
        ]
    elif num == 2:
        return [
            {"label": "4월 1주차", "me_api": 14, "all": 20},
            {"label": "4월 2주차", "me_api": 45, "all": 40},
            {"label": "4월 3주차", "me_api": 75, "all": 60},
            {"label": "4월 4주차", "me_api": 50, "all": 50},
            {"label": "4월 5주차", "me_api": 84, "all": 66},
            {"label": "5월 1주차", "me_api": 90, "all": 44},
            {"label": "5월 2주차", "me_api": 100, "all": 33},
            {"label": "5월 3주차", "me_api": 82, "all": 46},
            {"label": "5월 4주차", "me_api": 47, "all": 23},
            {"label": "6월 1주차", "me_api": 90, "all": 49},
            {"label": "6월 2주차", "me_api": 77, "all": 80},
            {"label": "6월 3주차", "me_api": 100, "all": 70},
            {"label": "6월 4주차", "me_api": 71, "all": 90},
            {"label": "6월 5주차", "me_api": 50, "all": 70},
        ]
    elif num == 3:
        return [
            {"label": "7월 1주차", "me_api": 14, "all": 20},
            {"label": "7월 2주차", "me_api": 45, "all": 40},
            {"label": "7월 3주차", "me_api": 75, "all": 60},
            {"label": "7월 4주차", "me_api": 50, "all": 50},
            {"label": "7월 5주차", "me_api": 84, "all": 66},
            {"label": "8월 1주차", "me_api": 90, "all": 44},
            {"label": "8월 2주차", "me_api": 100, "all": 33},
            {"label": "8월 3주차", "me_api": 82, "all": 46},
            {"label": "8월 4주차", "me_api": 47, "all": 23},
            {"label": "9월 1주차", "me_api": 90, "all": 49},
            {"label": "9월 2주차", "me_api": 77, "all": 80},
            {"label": "9월 3주차", "me_api": 100, "all": 70},
            {"label": "9월 4주차", "me_api": 71, "all": 90},
            {"label": "9월 5주차", "me_api": 50, "all": 70},
        ]
    else:
        return [
            {"label": "10월 1주차", "me_api": 14, "all": 20},
            {"label": "10월 2주차", "me_api": 45, "all": 40},
            {"label": "10월 3주차", "me_api": 75, "all": 60},
            {"label": "10월 4주차", "me_api": 50, "all": 50},
            {"label": "10월 5주차", "me_api": 84, "all": 66},
            {"label": "11월 1주차", "me_api": 90, "all": 44},
            {"label": "11월 2주차", "me_api": 100, "all": 33},
            {"label": "11월 3주차", "me_api": 82, "all": 46},
            {"label": "11월 4주차", "me_api": 47, "all": 23},
            {"label": "12월 1주차", "me_api": 90, "all": 49},
            {"label": "12월 2주차", "me_api": 77, "all": 80},
            {"label": "12월 3주차", "me_api": 100, "all": 70},
            {"label": "12월 4주차", "me_api": 71, "all": 90},
            {"label": "12월 5주차", "me_api": 50, "all": 70},
        ]


@router.get("/objectives", description="나의 목표", response_model=List[dict])
async def get_my_objectives(
    db: Session = Depends(get_db), user: User = Depends(check_user)
) -> List[dict]:
    return [
        {
            "objectiveId": 6,
            "objectiveTitle": "POKR 프로젝트 출시하기",
            "achievement": False,
            "keyResultPercent": 56,
            "initiativePercent": 77,
        },
        {
            "objectiveId": 17,
            "objectiveTitle": "바디프로필 찍기",
            "achievement": False,
            "keyResultPercent": 49,
            "initiativePercent": 80,
        },
        {
            "objectiveId": 63,
            "objectiveTitle": "북극곰 수영대회 나가기",
            "achievement": False,
            "keyResultPercent": 36,
            "initiativePercent": 40,
        },
    ]
