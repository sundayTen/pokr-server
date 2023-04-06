from datetime import datetime
from functools import reduce
from itertools import chain

from env import OBJECTIVE_WEIGHT
from schemas.metrics import ObjectiveAchievementPercentSchema
from schemas.objective import ObjectiveWithKeyResultsSchema


async def get_objective_achievement_percent(
    objective: ObjectiveWithKeyResultsSchema,
) -> ObjectiveAchievementPercentSchema:
    key_result_percent, initiative_percent = 0, 0
    key_results = objective.key_results
    initiatives = list(chain(*[key_result.initiatives for key_result in key_results]))

    if len(key_results):
        key_result_percent = reduce(
            lambda acc, x: acc + x.achievement_score, key_results, 0
        ) / len(key_results)

    if len(initiatives):
        initiative_percent = reduce(
            lambda acc, x: acc + (x.current_metrics / x.goal_metrics * 100),
            initiatives,
            0,
        ) / len(initiatives)

    return ObjectiveAchievementPercentSchema(
        objective_id=objective.id,
        objective_title=objective.title,
        achievement=objective.achievement,
        key_result_percent=key_result_percent,
        initiative_percent=initiative_percent,
    )


async def calculate_achievement_percent(objective: ObjectiveWithKeyResultsSchema):
    achievement_point, total_point = get_objective_achievement_percent(objective)
    key_results = objective.key_results
    initiatives = list(chain(*[key_result.initiatives for key_result in key_results]))
    # TODO 달성도 로직 만드는 중


async def get_objective_achievement_percent(objective: ObjectiveWithKeyResultsSchema):
    if datetime.now().year - 1 == objective.year:
        if objective.achievement:
            return OBJECTIVE_WEIGHT, OBJECTIVE_WEIGHT
        return 0, OBJECTIVE_WEIGHT
    return 0, 0
