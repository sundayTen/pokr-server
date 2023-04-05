from fastapi_camelcase import CamelModel


class ObjectiveAchievementPercentSchema(CamelModel):
    objective_id: int
    objective_title: str
    achievement: bool
    key_result_percent: int
    initiative_percent: int
