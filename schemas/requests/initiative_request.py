from datetime import date

from pydantic import BaseModel

from schemas.enums import Priority
from schemas.initiative import InitiativeSchema


class InitiativeCreateRequest(BaseModel):
    key_result_id: int
    title: str
    description: str | None
    open_date: date
    due_date: date
    goal_metrics: int
    priority: Priority

    def make_initiative_schema(self, current_metrics: int = 0):
        return InitiativeSchema(
            key_result_id=self.key_result_id,
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            priority=self.priority,
            goal_metrics=self.goal_metrics,
            current_metrics=current_metrics,
        )
