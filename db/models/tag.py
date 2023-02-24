from sqlalchemy import Column, Integer, String, ForeignKey

from db.config import Base
from db.models.common import DateBase


class Tag(Base, DateBase):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    objective_id = Column(
        Integer, ForeignKey("objective.id", ondelete="CASCADE"), nullable=False
    )
    tag = Column(String(300), nullable=False, index=True)
