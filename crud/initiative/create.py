from sqlalchemy.orm import Session

from schemas.initiative import InitiativeSchema


async def create_initiative(initiative_schema: InitiativeSchema, db: Session) -> int:
    initiative = initiative_schema.make_initiative()
    db.add(initiative)
    db.commit()

    return initiative.id
