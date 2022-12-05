from sqlalchemy import Column, Integer, String

from db.config import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(30), unique=True, index=True, nullable=False)
    name = Column(String(50))
    sns_key = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20), unique=True)
