from datetime import date

from pydantic import BaseModel

from schemas.key_result import KeyResultSchema


class KeyResultCreateRequest(BaseModel):
    objective_id: int
    title: str
    description: str | None
    open_date: date
    due_date: date

    def make_key_result_schema(self, achievement_score: int = 0):
        return KeyResultSchema(
            objective_id=self.objective_id,
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            achievement_score=achievement_score,
        )
