from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.config import get_db
from db.models.user import User

router = APIRouter()


@router.post("/signup", description="회원가입", response_model=dict)
async def signup(db: Session = Depends(get_db)):
    # 해당 로직은 crud 안에 있을텐데, 현재는 여기로 놓았음. 데이터가 생성될 때, 테이블이 같이 생성됨.
    u_data = User(email="123", sns_key="123", nickname="123")
    db.add(u_data)
    db.commit()

    return {"어떤 응답을": "줄 건지 생각해 오기"}
