from pydantic import BaseModel

from db.models.objective import Objective


class ObjectiveSchema(BaseModel):
    title: str
    year: int
    achievement: bool

    def make_objective(self, user_id: int) -> Objective:
        return Objective(
            user_id=user_id,
            title=self.title,
            year=self.year,
            achievement=self.achievement,
        )
