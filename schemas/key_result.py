from datetime import date
from typing import List

from pydantic import BaseModel

from db.models.key_result import KeyResult
from db.models.tag import Tag


class KeyResultSchema(BaseModel):
    objective_id: int
    title: str
    description: str
    open_date: date
    due_date: date
    achievement_score: int
    tags: List[str]

    def make_key_result(self) -> KeyResult:
        return KeyResult(
            objective_id=self.objective_id,
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            achievement_score=self.achievement_score,
            tags=[Tag(tag=tag) for tag in self.tags],
        )
