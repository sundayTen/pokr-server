from typing import List

from fastapi_camelcase import CamelModel

from db.models.objective import Objective
from schemas.key_result import KeyResultWithInitiativesSchema


class ObjectiveSchema(CamelModel):
    id: int | None
    title: str
    year: int
    achievement: bool

    def make_objective(self, user_id: int) -> Objective:
        return Objective(
            user_id=user_id,
            title=self.title,
            year=self.year,
            achievement=self.achievement,
        )


class ObjectiveWithKeyResultsSchema(ObjectiveSchema):
    key_results: List[KeyResultWithInitiativesSchema]

    def __init__(self, objective: Objective):
        super().__init__(
            id=objective.id,
            title=objective.title,
            year=objective.year,
            achievement=objective.achievement,
            tags=[tag.tag for tag in objective.tags],
            key_results=[
                KeyResultWithInitiativesSchema(key_result=key_result)
                for key_result in objective.key_results
            ],
        )


class ObjectiveNullableSchema(CamelModel):
    id: int | None
    title: str | None
    year: int | None
    achievement: bool | None

    async def update_objective(self, objective: Objective):
        objective.title = self.title if self.title else objective.title
        objective.year = self.year if self.year else objective.year
        objective.achievement = (
            self.achievement
            if self.achievement != objective.achievement
            else objective.achievement
        )
