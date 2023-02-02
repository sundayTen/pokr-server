from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.me.metrics.api import router as metrics_router
from db.config import get_db
from db.models.user import User
from jwt import check_user

router = APIRouter()
router.routes.extend(metrics_router.routes)


@router.get("/okr", description="OKR 전체 데이터 반환", response_model=List[dict])
async def get_my_okr(
    db: Session = Depends(get_db), user: User = Depends(check_user)
) -> List[dict]:
    return [
        {
            "objectiveId": 6,
            "objectiveTitle": "POKR 프로젝트 출시하기",
            "keyResult": [
                {
                    "keyResultId": 1,
                    "keyResultTitle": "목표달성 책 5권 보기",
                    "initiatives": [
                        {
                            "initiativeId": 1,
                            "initiativeTitle": "POKR 책 보기",
                            "achievement": False,
                        },
                        {
                            "initiativeId": 2,
                            "initiativeTitle": "타이탄의 도구들 책 보기",
                            "achievement": False,
                        },
                    ],
                },
                {
                    "keyResultId": 2,
                    "keyResultTitle": "아이폰 앱 검수 5단계 통과하기",
                    "initiatives": [
                        {
                            "initiativeId": 3,
                            "initiativeTitle": "1단계 통과",
                            "achievement": True,
                        },
                        {
                            "initiativeId": 4,
                            "initiativeTitle": "2단계 통과",
                            "achievement": False,
                        },
                    ],
                },
            ],
        },
        {
            "objectiveId": 17,
            "objectiveTitle": "바디프로필 찍기",
            "keyResult": [
                {
                    "keyResultId": 3,
                    "keyResultTitle": "dooooo it",
                    "initiatives": [
                        {
                            "initiativeId": 5,
                            "initiativeTitle": "do it",
                            "achievement": True,
                        },
                        {
                            "initiativeId": 6,
                            "initiativeTitle": "do it",
                            "achievement": False,
                        },
                    ],
                },
                {
                    "keyResultId": 4,
                    "keyResultTitle": "dooooo it",
                    "initiatives": [
                        {
                            "initiativeId": 7,
                            "initiativeTitle": "do it",
                            "achievement": True,
                        },
                        {
                            "initiativeId": 8,
                            "initiativeTitle": "do it",
                            "achievement": False,
                        },
                    ],
                },
            ],
        },
        {
            "objectiveId": 63,
            "objectiveTitle": "북극곰 수영대회 나가기",
            "keyResult": [
                {
                    "keyResultId": 5,
                    "keyResultTitle": "dooooo it",
                    "initiatives": [
                        {
                            "initiativeId": 9,
                            "initiativeTitle": "do it",
                            "achievement": True,
                        },
                        {
                            "initiativeId": 10,
                            "initiativeTitle": "do it",
                            "achievement": False,
                        },
                    ],
                },
                {
                    "keyResultId": 6,
                    "keyResultTitle": "dooooo it",
                    "initiatives": [
                        {
                            "initiativeId": 11,
                            "initiativeTitle": "do it",
                            "achievement": True,
                        },
                        {
                            "initiativeId": 12,
                            "initiativeTitle": "do it",
                            "achievement": False,
                        },
                    ],
                },
            ],
        },
    ]
