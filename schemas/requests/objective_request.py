from fastapi_camelcase import CamelModel
from pydantic import Field

from env import TITLE_MAX_LENGTH
from schemas.objective import ObjectiveSchema, ObjectiveNullableSchema


class ObjectiveCreateRequest(CamelModel):
    title: str = Field(max_length=TITLE_MAX_LENGTH)
    year: int = Field(ge=2023)

    def make_objective_schema(self, achievement: bool = False):
        return ObjectiveSchema(
            title=self.title, year=self.year, achievement=achievement
        )


class ObjectiveUpdateRequest(CamelModel):
    title: str | None = Field(max_length=TITLE_MAX_LENGTH)
    year: int | None = Field(ge=2023)
    achievement: bool | None

    def make_objective_nullable_schema(self):
        return ObjectiveNullableSchema(
            title=self.title,
            year=self.year,
            achievement=self.achievement,
        )
