from datetime import datetime, timedelta, date
from typing import List

from fastapi import Depends, Path, APIRouter
from fastapi.params import Query
from sqlalchemy.orm import Session

from crud.achievement_percent.read import get_achievement_percent
from db.config import get_db
from db.models.user import User
from jwt import check_user
from schemas.responses.achievement_percent_response import (
    AchievementPercentResponse,
    get_achievement_percent_response_by_label,
)
from service.metrics import (
    get_okr_achievement_percent,
)

router = APIRouter()


@router.get("/graph/half/{num}", description="나의 달성 수치[월별]")
async def get_my_monthly_metrics(
    num: int = Path(..., ge=1, le=2),
    year: int = Query(default=datetime.now().year, ge=2023),
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> List[AchievementPercentResponse]:
    achievement_percents = await get_achievement_percent(year, None, db)
    achievement_percents_of_user = await get_achievement_percent(year, user.id, db)
    achievement_percents_by_label = await get_achievement_percent_response_by_label(
        achievement_percents, achievement_percents_of_user
    )

    if num == 1:
        return [
            achievement_percents_by_label.get(label)
            if achievement_percents_by_label.get(label)
            else AchievementPercentResponse(label=label, me=0, all=0)
            for label in [f"{i}월" for i in range(1, 7)]
        ]

    return [
        achievement_percents_by_label.get(label)
        if achievement_percents_by_label.get(label)
        else AchievementPercentResponse(label=label, me=0, all=0)
        for label in [f"{i}월" for i in range(7, 13)]
    ]


@router.get("/graph/quarter/{num}", description="나의 달성 수치[주별]")
async def get_my_weekly_metrics(
    num: int = Path(..., ge=1, le=4),
    year: int = Query(default=datetime.now().year, ge=2023),
    db: Session = Depends(get_db),
    user: User = Depends(check_user),
) -> List[AchievementPercentResponse]:
    achievement_percents = await get_achievement_percent(year, None, db)
    achievement_percents_of_user = await get_achievement_percent(year, user.id, db)
    achievement_percents_by_label = await get_achievement_percent_response_by_label(
        achievement_percents, achievement_percents_of_user
    )

    my_achievement_percents = []
    start_date = date(year, num * 3 - 2, 1)
    week, cnt = 1, 0
    while cnt < 3:
        label = f"{start_date.month}월 {week}주차"
        if achievement_percents_by_label.get(label):
            my_achievement_percents.append(achievement_percents_by_label.get(label))
        else:
            my_achievement_percents.append(
                AchievementPercentResponse(label=label, me=0, all=0)
            )

        before = start_date
        start_date += timedelta(days=7)
        week += 1
        if start_date.month != before.month:
            week = 1
            cnt += 1

    return my_achievement_percents


@router.get("/objectives", description="나의 목표 달성 수치", response_model=List[dict])
async def get_my_objectives(user: User = Depends(check_user)) -> List[dict]:
    return [
        await get_okr_achievement_percent(objective) for objective in user.objectives
    ]
