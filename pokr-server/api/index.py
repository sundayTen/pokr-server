from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from db.models.user import User
from env import ADMIN_USER
from errors import CREDENTIALS_EXCEPTION
from jwt import check_user, create_access_token
from schemas.common import Token

router = APIRouter()


@router.get("/health", description="서버 상태 확인", response_model=str)
async def health_check() -> str:
    return "green"


@router.post(
    "/token", description="OAuth2 docs Authenticate Logic", response_model=Token
)
async def login_for_access_token(data: OAuth2PasswordRequestForm = Depends()):
    if data.username != ADMIN_USER:
        raise CREDENTIALS_EXCEPTION

    return Token(access_token=data.password, token_type="bearer")


@router.get("/auth-test", description="JWT 인증 테스트", response_model=int)
async def health_check(user: User = Depends(check_user)) -> int:
    return user.id


@router.get("/get-dummy-user", description="JWT 인증 테스트", response_model=Token)
async def health_check() -> Token:
    access_token: str = await create_access_token(User(id=1), 365)
    return Token(access_token=access_token, token_type="bearer")
