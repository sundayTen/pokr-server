from fastapi_camelcase import CamelModel

from schemas.objective import ObjectiveSchema, ObjectiveNullableSchema


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
    achievement: bool | None

    def make_objective_nullable_schema(self):
        return ObjectiveNullableSchema(
            title=self.title,
            year=self.year,
            achievement=self.achievement,
        )
