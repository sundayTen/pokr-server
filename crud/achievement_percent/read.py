from typing import List

from sqlalchemy.orm import Session

from db.models.acheivement_percent import AchievementPercent


async def get_achievement_percent(year: int, db: Session) -> List[AchievementPercent]:
    return db.query(AchievementPercent).filter_by(year=year)
