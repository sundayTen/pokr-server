from sqlalchemy.orm import Session

from db.models.user import User


async def get_user(user_id: int, db: Session) -> User:
    return db.query(User).get(user_id)


async def get_all_user(db: Session) -> User:
    return db.query(User).all()
