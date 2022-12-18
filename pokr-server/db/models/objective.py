from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from db.config import Base


class Objective(Base):
    __tablename__ = "objective"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(300), nullable=False)
    year = Column(Integer, nullable=False)
    achievement = Column(Boolean, nullable=False)
