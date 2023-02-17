from sqlalchemy.orm import Session

from schemas.objective import ObjectiveSchema


async def create_objective(
    user_id: int, objective_schema: ObjectiveSchema, db: Session
) -> int:
    objective = objective_schema.make_objective(user_id)
    db.add(objective)
    db.commit()

    return objective.id
