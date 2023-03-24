from sqlalchemy.orm import Session

from db.models.objective import Objective
from schemas.objective import ObjectiveNullableSchema


async def update_objective(
    objective_id: int, objective_schema: ObjectiveNullableSchema, db: Session
) -> None:
    objective = db.query(Objective).get(objective_id)
    await objective_schema.update_objective(objective)
    db.commit()
