from datetime import date

from fastapi_camelcase import CamelModel
from pydantic import Field

from env import TITLE_MAX_LENGTH, DESCRIPTION_MAX_LENGTH
from schemas.key_result import KeyResultSchema, KeyResultNullableSchema


class KeyResultCreateRequest(CamelModel):
    objective_id: int
    title: str = Field(max_length=TITLE_MAX_LENGTH)
    description: str | None = Field(max_length=DESCRIPTION_MAX_LENGTH)
    open_date: date
    due_date: date

    def make_key_result_schema(self, achievement_score: int = 0):
        return KeyResultSchema(
            objective_id=self.objective_id,
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            achievement_score=achievement_score,
        )


class KeyResultUpdateRequest(CamelModel):
    title: str | None = Field(max_length=TITLE_MAX_LENGTH)
    description: str | None = Field(max_length=DESCRIPTION_MAX_LENGTH)
    open_date: date | None
    due_date: date | None
    achievement_score: int | None = Field(ge=0, le=100)

    def make_key_result_nullable_schema(self):
        return KeyResultNullableSchema(
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            achievement_score=self.achievement_score,
        )
