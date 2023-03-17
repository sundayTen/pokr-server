from datetime import datetime

from fastapi_camelcase import CamelModel

from db.models.objective import Objective


async def make_objective_response(objective: Objective):
    return ObjectiveResponse(
        id=objective.id,
        title=objective.title,
        year=objective.year,
        achievement=objective.achievement,
        created_at=objective.created_at,
        updated_at=objective.updated_at,
    )


class ObjectiveResponse(CamelModel):
    id: int
    title: str
    year: int
    achievement: bool
    created_at: datetime
    updated_at: datetime
