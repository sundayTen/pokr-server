from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from db.config import Base
from db.models.memo import Memo


class Initiative(Base):
    __tablename__ = "initiative"

    id = Column(Integer, primary_key=True)
    keyresult_id = Column(Integer, ForeignKey("keyresult.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(300), nullable=False)
    description = Column(Text)
    priority = Column(Integer, nullable=False)
    metrics_info = Column(String(300))
    goal_metrics = Column(Integer, nullable=False)
    current_metrics = Column(Integer, nullable=False)

    initiatives = relationship(Memo.__name__, backref="initiative", passive_deletes=True)
