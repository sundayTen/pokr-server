from fastapi_camelcase import CamelModel

from schemas.objective import ObjectiveSchema


class ObjectiveCreateRequest(CamelModel):
    title: str
    year: int

    def make_objective_schema(self, achievement: bool = False):
        return ObjectiveSchema(
            title=self.title, year=self.year, achievement=achievement
        )


class ObjectiveUpdateRequest(CamelModel):
    title: str | None
    year: int | None
    achievement: bool | None  # 이거 비교는 기존 것과 같은 지를 확인.
