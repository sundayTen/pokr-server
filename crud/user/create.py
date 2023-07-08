from sqlalchemy.orm import Session

from crud.nickname.read import get_random_nickname
from db.models.user import User
from schemas.common import Platform


async def create_new_user(
    platform: Platform, encrypted_sns_key: str, db: Session
) -> User:
    nickname = await get_random_nickname(db)
    user = User(
        platform=platform,
        sns_key=encrypted_sns_key,
        nickname=nickname.nickname
        + (" " + str(nickname.count) if nickname.count else ""),
    )
    nickname.count += 1
    db.add(nickname)
    db.add(user)
    db.commit()

    return uesr
