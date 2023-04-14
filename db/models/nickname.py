from sqlalchemy import Column, Integer, String

from db.config import Base


class Nickname(Base):
    __tablename__ = "nickname"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(30), nullable=False, unique=True)
    count = Column(Integer, nullable=False)
