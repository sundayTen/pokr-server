from sqlalchemy import Column, Integer, String, ForeignKey

from db.config import Base
from db.models.common import DateBase


class Memo(Base, DateBase):
    __tablename__ = "memo"

    id = Column(Integer, primary_key=True)
    initiative_id = Column(
        Integer, ForeignKey("initiative.id", ondelete="CASCADE"), nullable=False
    )
    title = Column(String(300), nullable=False)
