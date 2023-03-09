from typing import List

from fastapi_camelcase import CamelModel

from schemas.objective import ObjectiveSchema


class ObjectiveCreateRequest(CamelModel):
    title: str
    year: int
    tags: List[str]

    def make_objective_schema(self, achievement: bool = False):
        return ObjectiveSchema(
            title=self.title, year=self.year, achievement=achievement, tags=self.tags
        )
