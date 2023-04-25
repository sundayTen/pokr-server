from datetime import datetime

from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date, JSON
from sqlalchemy.orm import relationship

from db.config import Base
from db.models.common import DateBase
from db.models.memo import Memo


class Initiative(Base, DateBase):
    __tablename__ = "initiative"

    id = Column(Integer, primary_key=True)
    key_result_id = Column(
        Integer, ForeignKey("key_result.id", ondelete="CASCADE"), nullable=False
    )
    title = Column(String(300), nullable=False)
    description = Column(Text)
    open_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)
    goal_metrics = Column(Integer, nullable=False)
    current_metrics = Column(Integer, nullable=False)
    done_times = Column(JSON)

    memos = relationship(Memo.__name__, backref="initiative", passive_deletes=False)

    async def copy(self) -> "Initiative":
        return Initiative(
            key_result_id=self.key_result_id,
            title=self.title,
            description=self.description,
            open_date=datetime.now().date(),
            due_date=datetime.now().date(),
            goal_metrics=self.goal_metrics,
            current_metrics=0,
        )
