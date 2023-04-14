from sqlmodel import Session

from db.models.nickname import Nickname


async def create_nickname(nickname: str, db: Session) -> None:
    db.add(Nickname(nickname=nickname, count=0))
    db.commit()
