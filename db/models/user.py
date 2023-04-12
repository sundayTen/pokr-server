from sqlalchemy import Column, Integer, String, UniqueConstraint
from sqlalchemy.orm import relationship

from db.config import Base
from db.models.acheivement_percent import AchievementPercent
from db.models.common import DateBase
from db.models.objective import Objective
from db.models.review import Review
from db.models.template import Template


class User(Base, DateBase):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(30), unique=True, index=True, nullable=False)
    name = Column(String(50))
    sns_key = Column(String(64), index=True, nullable=False)
    platform = Column(String(64), index=True, nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20), unique=True)
    UniqueConstraint("sns_key", "platform")

    objectives = relationship(Objective.__name__, backref="user", passive_deletes=False)
    templates = relationship(Template.__name__, backref="user", passive_deletes=False)
    reviews = relationship(Review.__name__, backref="user", passive_deletes=False)
    achievement_percents = relationship(
        AchievementPercent.__name__, backref="user", passive_deletes=False
    )
