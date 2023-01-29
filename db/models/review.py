from sqlalchemy import Column, Integer, String, ForeignKey, Text

from db.config import Base


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    year = Column(Integer, nullable=False)
    quarter = Column(Integer)
    title = Column(String(300), nullable=False)
    content = Column(Text, nullable=False)
