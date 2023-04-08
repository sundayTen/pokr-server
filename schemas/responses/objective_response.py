from datetime import datetime

from fastapi_camelcase import CamelModel

from db.models.objective import Objective


async def make_objective_response(objective: Objective):
    return ObjectiveResponse(
        id=objective.id,
        title=objective.title,
        year=objective.year,
        achievement=objective.achievement,
        key_result_count=len(objective.key_results),
        initiative_count=sum(
            [len(key_result.initiatives) for key_result in objective.key_results]
        ),
        created_at=objective.created_at,
        updated_at=objective.updated_at,
    )


class ObjectiveResponse(CamelModel):
    id: int
    title: str
    year: int
    achievement: bool
    key_result_count: int
    initiative_count: int
    created_at: datetime
    updated_at: datetime
