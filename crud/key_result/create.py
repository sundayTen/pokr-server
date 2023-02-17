from sqlalchemy.orm import Session

from schemas.key_result import KeyResultSchema


async def create_key_result(key_result_schema: KeyResultSchema, db: Session) -> int:
    key_result = key_result_schema.make_key_result()
    db.add(key_result)
    db.commit()

    return key_result.id
