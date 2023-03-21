from datetime import date
from typing import List

from fastapi_camelcase import CamelModel

from db.models.objective import Objective
from schemas.objective import ObjectiveWithKeyResultsSchema


async def make_okr_response(
    objectives: List[Objective],
) -> List[ObjectiveWithKeyResultsSchema]:
    return [
        ObjectiveWithKeyResultsSchema(objective=objective) for objective in objectives
    ]


class OkrInitiativeResponse(CamelModel):
    id: int
    title: str
    description: str | None
    open_date: date
    due_date: date
    goal_metrics: int
    current_metrics: int


class OkrKeyResultResponse(CamelModel):
    id: int
    title: str
    description: str | None
    open_date: date
    due_date: date
    achievement_score: int
    initiatives: List[OkrInitiativeResponse]


class OkrObjectiveResponse(CamelModel):
    id: int
    title: str
    year: int
    achievement: bool
    key_results: List[OkrKeyResultResponse]
