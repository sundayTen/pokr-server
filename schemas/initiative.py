from datetime import date

from fastapi_camelcase import CamelModel

from db.models.initiative import Initiative


class InitiativeSchema(CamelModel):
    id: int | None
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


class InitiativeNullableSchema(CamelModel):
    id: int | None
    key_result_id: int | None
    title: str | None
    description: str | None
    open_date: date | None
    due_date: date | None
    goal_metrics: int | None
    current_metrics: int | None

    async def update_initiative(self, initiative: Initiative):
        initiative.title = self.title if self.title else initiative.title
        initiative.description = (
            self.description if self.description else initiative.description
        )
        initiative.open_date = (
            self.open_date if self.open_date else initiative.open_date
        )
        initiative.due_date = self.due_date if self.due_date else initiative.due_date
        initiative.goal_metrics = (
            self.goal_metrics if self.goal_metrics else initiative.goal_metrics
        )
        initiative.current_metrics = (
            self.current_metrics if self.current_metrics else initiative.current_metrics
        )
