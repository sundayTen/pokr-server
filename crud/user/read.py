from sqlalchemy.orm import Session

from db.models.user import User
from schemas.common import Platform


async def get_user(user_id: int, db: Session) -> User:
    return db.query(User).get(user_id)


async def get_all_user(db: Session) -> User:
    return db.query(User).all()


async def get_user_by_platform_and_sns_key(
    platform: Platform, encrypted_sns_key: str, db: Session
) -> User:
    return (
        db.query(User).filter(platform=platform.name, sns_key=encrypted_sns_key).first()
    )
