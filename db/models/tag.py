from sqlalchemy import Column, Integer, String, ForeignKey

from db.config import Base
from db.models.common import DateBase


class Tag(Base, DateBase):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True)
    key_result_id = Column(
        Integer, ForeignKey("key_result.id", ondelete="CASCADE"), nullable=False
    )
    tag = Column(String(300), nullable=False, index=True)
