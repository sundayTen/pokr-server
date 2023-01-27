from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.config import get_db
from db.models.user import User
from jwt import check_user

router = APIRouter()


@router.post("/metrics", description="나의 달성 수치", response_model=dict)
async def get_my_metrics(
    db: Session = Depends(get_db), user: User = Depends(check_user)
) -> dict:
    return {
        "Objective": 34,
        "Key-result": 56,
        "Initiative": 77,
        "monthly": [0, 20, 40, 77, 100, 30, 60, 0, 0, 10, 87, 43],
    }


@router.post("/objectives", description="나의 목표", response_model=dict)
async def get_my_objectives(
    db: Session = Depends(get_db), user: User = Depends(check_user)
) -> dict:
    return {"Objectives": ["POKR 프로젝트 출시하기", "바디프로필 찍기", "북극곰 수영대회 나가기"]}
