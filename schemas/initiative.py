from datetime import date

from fastapi_camelcase import CamelModel

from db.models.initiative import Initiative


class InitiativeSchema(CamelModel):
    key_result_id: int
    title: str
    description: str | None
    open_date: date
    due_date: date
    goal_metrics: int
    current_metrics: int

    def make_initiative(self) -> Initiative:
        return Initiative(
            key_result_id=self.key_result_id,
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            goal_metrics=self.goal_metrics,
            current_metrics=self.current_metrics,
        )
