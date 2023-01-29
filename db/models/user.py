from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db.config import Base
from db.models.objective import Objective
from db.models.review import Review
from db.models.template import Template


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    nickname = Column(String(30), unique=True, index=True, nullable=False)
    name = Column(String(50))
    sns_key = Column(String(64), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True)
    phone = Column(String(20), unique=True)

    objectives = relationship(Objective.__name__, backref="user", passive_deletes=True)
    templates = relationship(Template.__name__, backref="user", passive_deletes=True)
    reviews = relationship(Review.__name__, backref="user", passive_deletes=True)
