from sqlalchemy.orm import Session

from db.models.key_result import KeyResult


async def delete_key_result(key_result_id: int, db: Session) -> None:
    db.query(KeyResult).filter(KeyResult.id == key_result_id).delete()
    db.commit()
