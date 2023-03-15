from sqlalchemy.orm import Session

from db.models.objective import Objective


async def delete_objective(objective_id: int, db: Session) -> None:
    db.query(Objective).filter(Objective.id == objective_id).delete()
    db.commit()
