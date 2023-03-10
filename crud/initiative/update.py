from sqlalchemy.orm import Session

from db.models.initiative import Initiative


async def done_initiative(initiative_id: int, db: Session, count: int) -> None:
    initiative = db.query(Initiative).get(initiative_id)
    initiative.current_metrics += count
    db.commit()
