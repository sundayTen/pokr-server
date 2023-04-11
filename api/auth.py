from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.config import get_db
from db.models.user import User
from env import JWT_PREFIX
from jwt import create_access_token
from schemas.requests.auth_request import NaverSignupRequest
from schemas.responses.common_response import TokenResponse

router = APIRouter()


@router.post("/login/naver", description="네이버 회원가입 및 로그인", status_code=200)
async def signup(
    naver_signup_request: NaverSignupRequest, db: Session = Depends(get_db)
) -> TokenResponse:
    naver_signup_request.access_token  # TODO 네이버에서 데이터 가져오기.
    # TODO 이미 유저가 있는지 확인
    user = None
    # TODO sns 값 암호화, 플랫폼 추가, 랜덤 닉네임 설정
    if not user:
        user = User(sns_key="platform_id", nickname="random_nickname")
        db.add(user)
        db.commit()

    return TokenResponse(access_token=create_access_token(user), token_type=JWT_PREFIX)
