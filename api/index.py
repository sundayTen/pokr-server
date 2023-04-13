from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from db.models.user import User
from env import ADMIN_USER, JWT_PREFIX
from errors import CREDENTIALS_EXCEPTION
from jwt import create_access_token
from schemas.common import Token

router = APIRouter()


@router.get("/health", description="서버 상태 확인", response_model=str)
async def health_check() -> str:
    return "green"


@router.post("/token", description="OAuth2 docs Authenticate Logic")
async def login_for_access_token(data: OAuth2PasswordRequestForm = Depends()) -> Token:
    if data.username != ADMIN_USER:
        raise CREDENTIALS_EXCEPTION

    return Token(access_token=data.password, token_type=JWT_PREFIX)


@router.get("/get-dummy-user", description="JWT 더미 유저 생성")
async def get_dummy_user() -> Token:
    access_token: str = await create_access_token(User(id=1), 365)
    return Token(access_token=access_token, token_type=JWT_PREFIX)
