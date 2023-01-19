from datetime import datetime, timedelta

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

from crud.user.read import get_user
from db.config import get_db
from db.models.user import User
from env import JWT_SECRET_KEY, JWT_ALGORITHM
from errors import CREDENTIALS_EXCEPTION

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def check_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except JWTError:
        raise CREDENTIALS_EXCEPTION

    user_id: str = payload.get("id")
    if user_id is None:
        raise CREDENTIALS_EXCEPTION

    user: User = await get_user(user_id, db)
    if user is None:
        raise CREDENTIALS_EXCEPTION

    return user


async def create_access_token(user: User, days: float = 30) -> str:
    payload = dict()
    payload["id"] = user.id
    payload["name"] = user.name
    payload["nickname"] = user.nickname
    payload["email"] = user.email
    payload["exp"] = datetime.utcnow() + timedelta(days=days)

    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
