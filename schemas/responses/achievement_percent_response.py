from fastapi_camelcase import CamelModel


class AchievementPercentResponse(CamelModel):
    label: str
    me: int
    all: int
