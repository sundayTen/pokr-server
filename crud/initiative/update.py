from sqlalchemy.orm import Session

from db.models.initiative import Initiative
from schemas.initiative import InitiativeNullableSchema


async def done_initiative(initiative_id: int, db: Session, count: int) -> None:
    initiative = db.query(Initiative).get(initiative_id)
    initiative.current_metrics += count
    db.commit()


async def update_initiative(
    initiative_id: int, initiative_schema: InitiativeNullableSchema, db: Session
) -> None:
    initiative = db.query(Initiative).get(initiative_id)
    await initiative_schema.update_initiative(initiative)
    db.commit()
