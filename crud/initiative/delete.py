from sqlalchemy.orm import Session

from db.models.initiative import Initiative


async def delete_initiative(initiative_id: int, db: Session) -> None:
    db.query(Initiative).filter(Initiative.id == initiative_id).delete()
    db.commit()
