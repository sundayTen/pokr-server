from sqlalchemy.orm import Session

from db.models.objective import Objective
from schemas.objective import ObjectiveSchema


async def create_objective(
    user_id: int, objective_schema: ObjectiveSchema, db: Session
) -> int:
    objective = objective_schema.make_objective(user_id)
    db.add(objective)
    db.commit()

    return objective.id


async def copy_objective(objective: Objective, db: Session) -> int:
    copied_objective = await objective.copy()
    db.add(copied_objective)
    db.commit()

    return copied_objective.id
