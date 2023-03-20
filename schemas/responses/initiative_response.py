from datetime import datetime, date

from fastapi_camelcase import CamelModel

from db.models.initiative import Initiative


async def make_initiative_response(initiative: Initiative):
    return InitiativeResponse(
        id=initiative.id,
        key_result_id=initiative.key_result_id,
        title=initiative.title,
        description=initiative.description,
        open_date=initiative.open_date,
        due_date=initiative.due_date,
        goal_metrics=initiative.goal_metrics,
        current_metrics=initiative.current_metrics,
        created_at=initiative.created_at,
        updated_at=initiative.updated_at,
    )


class InitiativeResponse(CamelModel):
    id: int
    key_result_id: int
    title: str
    description: str | None
    open_date: date
    due_date: date
    goal_metrics: int
    current_metrics: int
    created_at: datetime
    updated_at: datetime
