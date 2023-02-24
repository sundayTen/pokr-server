from typing import List

from pydantic import BaseModel

from db.models.objective import Objective
from db.models.tag import Tag


class ObjectiveSchema(BaseModel):
    title: str
    year: int
    achievement: bool
    tags: List[str]

    def make_objective(self, user_id: int) -> Objective:
        return Objective(
            user_id=user_id,
            title=self.title,
            year=self.year,
            achievement=self.achievement,
            tags=[Tag(tag=tag) for tag in self.tags],
        )
