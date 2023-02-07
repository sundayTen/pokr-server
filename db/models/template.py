from sqlalchemy import Column, Integer, ForeignKey, JSON

from db.config import Base
from db.models.common import DateBase


class Template(Base, DateBase):
    __tablename__ = "template"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    snapshot = Column(JSON, nullable=False)


class TemplateLike(Base):
    __tablename__ = "template_like"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    template_id = Column(
        Integer, ForeignKey("template.id", ondelete="CASCADE"), nullable=False
    )
