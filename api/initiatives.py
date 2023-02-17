from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.config import get_db
from db.models.user import User
from jwt import check_user

router = APIRouter()


@router.post("/done/{initiative_id}", description="주요 행동 완료", response_model=None)
async def initiative_done(
    initiative_id: int, db: Session = Depends(get_db), user: User = Depends(check_user)
) -> None:
    return
