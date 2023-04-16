from random import random

from sqlalchemy.orm import Session

from db.models.nickname import Nickname


async def get_random_nickname(db: Session):
    latest_nickname = db.query(Nickname).order_by(Nickname.id.desc()).first()
    random_number = (random() * 10000 % latest_nickname.id) + 1
    nickname = (
        db.query(Nickname)
        .filter(Nickname.id >= random_number)
        .order_by(Nickname.id.desc())
        .first()
    )
    if nickname:
        return nickname
    return (
        db.query(Nickname)
        .filter(Nickname.id <= random_number)
        .order_by(Nickname.id.asc())
        .first()
    )
