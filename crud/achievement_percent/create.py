from sqlalchemy.orm import Session

from schemas.achievement_percent import AchievementPercentSchema


async def create_achievement_percent(
    achievement_percent_schema: AchievementPercentSchema, db: Session
) -> int:
    achievement_percent = await achievement_percent_schema.make_achievement_percent()
    db.add(achievement_percent)
    db.commit()

    return achievement_percent.id
