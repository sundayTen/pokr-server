from typing import List

from fastapi_camelcase import CamelModel

from db.models.objective import Objective
from schemas.key_result import KeyResultWithInitiativesSchema


class ObjectiveSchema(CamelModel):
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
            title=objective.title,
            year=objective.year,
            achievement=objective.achievement,
            tags=[tag.tag for tag in objective.tags],
            key_results=[
                KeyResultWithInitiativesSchema(key_result=key_result)
                for key_result in objective.key_results
            ],
        )
