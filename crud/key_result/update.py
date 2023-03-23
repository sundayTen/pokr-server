from sqlalchemy.orm import Session

from db.models.key_result import KeyResult
from schemas.key_result import KeyResultNullableSchema


async def update_key_result(
    key_result_id: int, key_result_schema: KeyResultNullableSchema, db: Session
) -> None:
    key_result = db.query(KeyResult).get(key_result_id)
    await key_result_schema.update_key_result(key_result)
    db.commit()
