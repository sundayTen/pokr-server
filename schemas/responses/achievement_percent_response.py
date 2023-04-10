from typing import List, Dict

from fastapi_camelcase import CamelModel

from db.models.acheivement_percent import AchievementPercent


class AchievementPercentResponse(CamelModel):
    label: str
    me: int
    all: int


async def get_achievement_percent_response_by_label(
    achievement_percents: List[AchievementPercent],
    achievement_percents_of_user: List[AchievementPercent],
) -> Dict[str, AchievementPercentResponse]:
    achievement_percents_by_label = dict()
    for achievement_percent in achievement_percents_of_user:
        achievement_percents_by_label[
            achievement_percent.label
        ] = AchievementPercentResponse(
            label=achievement_percent.label, me=achievement_percent.percent, all=0
        )

    for achievement_percent in achievement_percents:
        if achievement_percents_by_label.get(achievement_percent.label):
            achievement_percents_by_label[
                achievement_percent.label
            ].all = achievement_percent.percent

    return achievement_percents_by_label
