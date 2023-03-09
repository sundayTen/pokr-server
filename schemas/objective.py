from typing import List

from pydantic import BaseModel

from db.models.objective import Objective
from db.models.tag import Tag
from schemas.key_result import KeyResultWithInitiativesSchema


class ObjectiveSchema(BaseModel):
    title: str
    year: int
    achievement: bool
    tags: List[str]

    def make_objective(self, user_id: int) -> Objective:
        return Objective(
            user_id=user_id,
            title=self.title,
            year=self.year,
            achievement=self.achievement,
            tags=[Tag(tag=tag) for tag in self.tags],
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
