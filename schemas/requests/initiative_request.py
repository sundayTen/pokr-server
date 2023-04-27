from datetime import date

from fastapi_camelcase import CamelModel
from pydantic import Field

from env import DESCRIPTION_MAX_LENGTH, TITLE_MAX_LENGTH
from schemas.initiative import InitiativeSchema, InitiativeNullableSchema


class InitiativeCreateRequest(CamelModel):
    key_result_id: int
    title: str = Field(max_length=TITLE_MAX_LENGTH)
    description: str | None = Field(max_length=DESCRIPTION_MAX_LENGTH)
    open_date: date
    due_date: date
    goal_metrics: int = Field(ge=1)

    def make_initiative_schema(self, current_metrics: int = 0):
        return InitiativeSchema(
            key_result_id=self.key_result_id,
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            goal_metrics=self.goal_metrics,
            current_metrics=current_metrics,
        )


class InitiativeUpdateRequest(CamelModel):
    title: str | None = Field(max_length=TITLE_MAX_LENGTH)
    description: str | None = Field(max_length=DESCRIPTION_MAX_LENGTH)
    open_date: date | None
    due_date: date | None
    goal_metrics: int | None = Field(ge=1)
    current_metrics: int | None = Field(ge=0)

    def make_initiative_nullable_schema(self):
        return InitiativeNullableSchema(
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            goal_metrics=self.goal_metrics,
            current_metrics=self.current_metrics,
        )
