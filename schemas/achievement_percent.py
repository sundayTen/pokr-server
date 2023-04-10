from fastapi_camelcase import CamelModel

from db.models.acheivement_percent import AchievementPercent
from schemas.common import PeriodCategory


class AchievementPercentSchema(CamelModel):
    id: int | None
    user_id: int | None
    year: int
    category: PeriodCategory
    label: str
    percent: int

    async def make_achievement_percent(self):
        return AchievementPercent(
            user_id=self.user_id,
            year=self.year,
            category=self.category.name,
            label=self.label,
            percent=self.percent,
        )
