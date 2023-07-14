from sqlalchemy.orm import Session

from db.models.initiative import Initiative
from schemas.initiative import InitiativeNullableSchema, update_done_times


async def done_initiative(initiative_id: int, db: Session, count: int) -> bool:
    initiative = db.query(Initiative).get(initiative_id)
    initiative.current_metrics += count
    if initiative.current_metrics < 0:
        return False

    initiative.done_times = await update_done_times(
        initiative, initiative.current_metrics
    )
    db.commit()

    return True


async def update_initiative(
    initiative_id: int, initiative_schema: InitiativeNullableSchema, db: Session
) -> None:
    initiative = db.query(Initiative).get(initiative_id)
    await initiative_schema.update_initiative(initiative)
    db.commit()
