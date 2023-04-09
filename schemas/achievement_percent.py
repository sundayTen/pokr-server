from fastapi_camelcase import CamelModel

from db.models.acheivement_percent import AchievementPercent
from schemas.common import PeriodCategory


class AchievementPercentSchema(CamelModel):
    id: int | None
    year: int
    category: PeriodCategory
    label: str
    percent_of_users: int

    async def make_achievement_percent(self):
        return AchievementPercent(
            year=self.year,
            category=self.category.name,
            label=self.label,
            percent_of_users=self.percent_of_users,
        )
