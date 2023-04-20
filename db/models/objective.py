from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from db.config import Base
from db.models.common import DateBase
from db.models.key_result import KeyResult
from db.models.tag import Tag


class Objective(Base, DateBase):
    __tablename__ = "objective"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(300), nullable=False)
    year = Column(Integer, nullable=False)
    achievement = Column(Boolean, nullable=False)

    tags = relationship(Tag.__name__, backref="objective", passive_deletes=True)
    key_results = relationship(
        KeyResult.__name__, backref="objective", passive_deletes=False
    )

    async def copy(self) -> "Objective":
        return Objective(
            user_id=self.user_id,
            title=self.title,
            year=datetime.now().year,
            achievement=False,
        )
