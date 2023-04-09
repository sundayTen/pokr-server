from typing import List

from fastapi import Depends, Path, APIRouter
from sqlalchemy.orm import Session

from crud.achievement_percent.read import get_achievement_percent
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.responses.achievement_percent_response import AchievementPercentResponse
from service.metrics import get_objective_achievement_percent

router = APIRouter()


@router.get("/graph/half/{num}", description="나의 달성 수치[월별]", response_model=List[dict])
async def get_my_monthly_metrics(
    num: int = Path(..., ge=1, le=2),
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> List[dict]:
    achievement_percents = await get_achievement_percent(2023, db)
    my_achievement_percents = []
    achievement_percents_by_label = dict()
    for achievement_percent in achievement_percents:
        achievement_percents_by_label[
            achievement_percent.label
        ] = AchievementPercentResponse(
            label=achievement_percent.label,
            me=999,
            all=achievement_percent.percent_of_users,
        )

    if num == 1:
        for label in [f"{i}월" for i in range(1, 7)]:
            if achievement_percents_by_label.get(label):
                my_achievement_percents.append(achievement_percents_by_label.get(label))
            else:
                my_achievement_percents.append(
                    AchievementPercentResponse(
                        label=label,
                        me=99,
                        all=0,
                    )
                )
    else:
        for label in [f"{i}월" for i in range(7, 13)]:
            if achievement_percents_by_label.get(label):
                my_achievement_percents.append(achievement_percents_by_label.get(label))
            else:
                my_achievement_percents.append(
                    AchievementPercentResponse(
                        label=label,
                        me=99,
                        all=0,
                    )
                )

    return my_achievement_percents


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
            {"label": "1월 1주차", "me": 14, "all": 20},
            {"label": "1월 2주차", "me": 45, "all": 40},
            {"label": "1월 3주차", "me": 75, "all": 60},
            {"label": "1월 4주차", "me": 50, "all": 50},
            {"label": "1월 5주차", "me": 84, "all": 66},
            {"label": "2월 1주차", "me": 90, "all": 44},
            {"label": "2월 2주차", "me": 100, "all": 33},
            {"label": "2월 3주차", "me": 82, "all": 46},
            {"label": "2월 4주차", "me": 47, "all": 23},
            {"label": "3월 1주차", "me": 90, "all": 49},
            {"label": "3월 2주차", "me": 77, "all": 80},
            {"label": "3월 3주차", "me": 100, "all": 70},
            {"label": "3월 4주차", "me": 71, "all": 90},
            {"label": "3월 5주차", "me": 50, "all": 70},
        ]
    elif num == 2:
        return [
            {"label": "4월 1주차", "me": 14, "all": 20},
            {"label": "4월 2주차", "me": 45, "all": 40},
            {"label": "4월 3주차", "me": 75, "all": 60},
            {"label": "4월 4주차", "me": 50, "all": 50},
            {"label": "4월 5주차", "me": 84, "all": 66},
            {"label": "5월 1주차", "me": 90, "all": 44},
            {"label": "5월 2주차", "me": 100, "all": 33},
            {"label": "5월 3주차", "me": 82, "all": 46},
            {"label": "5월 4주차", "me": 47, "all": 23},
            {"label": "6월 1주차", "me": 90, "all": 49},
            {"label": "6월 2주차", "me": 77, "all": 80},
            {"label": "6월 3주차", "me": 100, "all": 70},
            {"label": "6월 4주차", "me": 71, "all": 90},
            {"label": "6월 5주차", "me": 50, "all": 70},
        ]
    elif num == 3:
        return [
            {"label": "7월 1주차", "me": 14, "all": 20},
            {"label": "7월 2주차", "me": 45, "all": 40},
            {"label": "7월 3주차", "me": 75, "all": 60},
            {"label": "7월 4주차", "me": 50, "all": 50},
            {"label": "7월 5주차", "me": 84, "all": 66},
            {"label": "8월 1주차", "me": 90, "all": 44},
            {"label": "8월 2주차", "me": 100, "all": 33},
            {"label": "8월 3주차", "me": 82, "all": 46},
            {"label": "8월 4주차", "me": 47, "all": 23},
            {"label": "9월 1주차", "me": 90, "all": 49},
            {"label": "9월 2주차", "me": 77, "all": 80},
            {"label": "9월 3주차", "me": 100, "all": 70},
            {"label": "9월 4주차", "me": 71, "all": 90},
            {"label": "9월 5주차", "me": 50, "all": 70},
        ]
    else:
        return [
            {"label": "10월 1주차", "me": 14, "all": 20},
            {"label": "10월 2주차", "me": 45, "all": 40},
            {"label": "10월 3주차", "me": 75, "all": 60},
            {"label": "10월 4주차", "me": 50, "all": 50},
            {"label": "10월 5주차", "me": 84, "all": 66},
            {"label": "11월 1주차", "me": 90, "all": 44},
            {"label": "11월 2주차", "me": 100, "all": 33},
            {"label": "11월 3주차", "me": 82, "all": 46},
            {"label": "11월 4주차", "me": 47, "all": 23},
            {"label": "12월 1주차", "me": 90, "all": 49},
            {"label": "12월 2주차", "me": 77, "all": 80},
            {"label": "12월 3주차", "me": 100, "all": 70},
            {"label": "12월 4주차", "me": 71, "all": 90},
            {"label": "12월 5주차", "me": 50, "all": 70},
        ]


@router.get("/objectives", description="나의 목표 달성 수치", response_model=List[dict])
async def get_my_objectives(user: User = Depends(check_user)) -> List[dict]:
    return [
        await get_objective_achievement_percent(objective)
        for objective in user.objectives
    ]
