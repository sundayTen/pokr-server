from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from db.config import Base
from db.models.common import DateBase
from db.models.initiative import Initiative


class KeyResult(Base, DateBase):
    __tablename__ = "key_result"

    id = Column(Integer, primary_key=True)
    objective_id = Column(
        Integer, ForeignKey("objective.id", ondelete="CASCADE"), nullable=False
    )
    title = Column(String(300), nullable=False)
    description = Column(Text)
    open_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    achievement_score = Column(Integer, nullable=False)

    initiatives = relationship(
        Initiative.__name__, backref="key_result", passive_deletes=False
    )
