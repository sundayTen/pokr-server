from datetime import date
from typing import List

from fastapi_camelcase import CamelModel

from db.models.key_result import KeyResult
from schemas.initiative import InitiativeSchema


class KeyResultSchema(CamelModel):
    objective_id: int
    title: str
    description: str
    open_date: date
    due_date: date
    achievement_score: int

    def make_key_result(self) -> KeyResult:
        return KeyResult(
            objective_id=self.objective_id,
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            achievement_score=self.achievement_score,
        )


class KeyResultWithInitiativesSchema(KeyResultSchema):
    initiatives: List[InitiativeSchema]

    def __init__(self, key_result: KeyResult) -> None:
        super().__init__(
            objective_id=key_result.objective_id,
            title=key_result.title,
            description=key_result.description,
            open_date=key_result.open_date,
            due_date=key_result.due_date,
            achievement_score=key_result.achievement_score,
            initiatives=[
                InitiativeSchema(
                    key_result_id=initiative.key_result_id,
                    title=initiative.title,
                    description=initiative.description,
                    open_date=initiative.open_date,
                    due_date=initiative.due_date,
                    goal_metrics=initiative.goal_metrics,
                    current_metrics=initiative.current_metrics,
                )
                for initiative in key_result.initiatives
            ],
        )
