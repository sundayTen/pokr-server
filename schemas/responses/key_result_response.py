from datetime import date, datetime

from fastapi_camelcase import CamelModel

from db.models.key_result import KeyResult


async def make_key_result_response(key_result: KeyResult):
    return KeyResultResponse(
        id=key_result.id,
        objective_id=key_result.objective_id,
        title=key_result.title,
        description=key_result.description,
        open_date=key_result.open_date,
        due_date=key_result.due_date,
        achievement_score=key_result.achievement_score,
        created_at=key_result.created_at,
        updated_at=key_result.updated_at,
    )


class KeyResultResponse(CamelModel):
    id: int
    objective_id: int
    title: str
    description: str | None
    open_date: date
    due_date: date
    achievement_score: int
    created_at: datetime
    updated_at: datetime
