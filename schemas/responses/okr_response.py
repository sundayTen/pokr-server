from typing import List

from db.models.objective import Objective
from schemas.objective import ObjectiveWithKeyResultsSchema


def make_okr_response(
    objectives: List[Objective],
) -> List[ObjectiveWithKeyResultsSchema]:
    return [
        ObjectiveWithKeyResultsSchema(objective=objective) for objective in objectives
    ]
