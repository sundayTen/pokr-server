from pydantic import BaseModel

from schemas.objective import ObjectiveSchema


class ObjectiveCreateRequest(BaseModel):
    title: str
    year: int

    def make_objective_schema(self):
        return ObjectiveSchema(title=self.title, year=self.year, achievement=False)
