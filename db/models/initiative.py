from sqlalchemy import Column, Integer, String, Text, ForeignKey
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
    priority = Column(Integer, nullable=False)
    metrics_info = Column(String(30))
    goal_metrics = Column(Integer, nullable=False)
    current_metrics = Column(Integer, nullable=False)

    memos = relationship(Memo.__name__, backref="initiative", passive_deletes=True)
