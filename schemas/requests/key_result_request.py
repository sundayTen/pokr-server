from datetime import date

from fastapi_camelcase import CamelModel

from schemas.key_result import KeyResultSchema, KeyResultNullableSchema


class KeyResultCreateRequest(CamelModel):
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


class KeyResultUpdateRequest(CamelModel):
    title: str | None
    description: str | None
    open_date: date | None
    due_date: date | None
    achievement_score: int | None

    def make_key_result_nullable_schema(self):
        return KeyResultNullableSchema(
            title=self.title,
            description=self.description,
            open_date=self.open_date,
            due_date=self.due_date,
            achievement_score=self.achievement_score,
        )
