from datetime import date
from typing import List

from schemas.objective import ObjectiveWithKeyResultsSchema


async def filter_okr(
    start_date: date, end_date: date, okrs: List[ObjectiveWithKeyResultsSchema]
):
    filtered_okrs = list(
        filter(lambda x: start_date.year <= x.year <= end_date.year, okrs)
    )
    for objective in filtered_okrs:
        objective.key_results = list(
            filter(
                lambda x: end_date >= x.open_date and start_date <= x.due_date,
                objective.key_results,
            )
        )
        for key_result in objective.key_results:
            key_result.initiatives = list(
                filter(
                    lambda x: end_date >= x.open_date and start_date <= x.due_date,
                    key_result.initiatives,
                )
            )

    return filtered_okrs
