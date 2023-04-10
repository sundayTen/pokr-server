from sqlalchemy import Column, Integer, String, ForeignKey

from db.config import Base


class AchievementPercent(Base):
    __tablename__ = "achievement_percent"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    year = Column(Integer, nullable=False)
    category = Column(String(20), nullable=False)
    label = Column(String(100), nullable=False)
    percent_of_users = Column(Integer, nullable=False)
