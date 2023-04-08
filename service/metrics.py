import time
from datetime import datetime
from functools import reduce
from itertools import chain
from typing import List

from env import (
    OBJECTIVE_WEIGHT,
    KEY_RESULT_WEIGHT,
    KEY_RESULT_MAX_SCORE,
    INITIATIVE_WEIGHT,
)
from schemas.common import PeriodCategory
from schemas.initiative import InitiativeSchema
from schemas.key_result import KeyResultWithInitiativesSchema
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


async def calculate_achievement_percent(
    objectives: List[ObjectiveWithKeyResultsSchema], category: PeriodCategory
):
    point, total_point = 0, 0
    for objective in objectives:
        key_results = objective.key_results
        initiatives = list(
            chain(*[key_result.initiatives for key_result in key_results])
        )
        points_for_calculating_percent = [
            await get_objective_achievement_percent(objective, category),
            await get_key_results_achievement_percent(key_results, category),
            await get_initiatives_achievement_percent(initiatives, category),
        ]

        point += sum([points[0] for points in points_for_calculating_percent])
        total_point += sum([points[1] for points in points_for_calculating_percent])

    if total_point:
        return int(point / total_point * 100)
    return 0


async def get_objective_achievement_percent(
    objective: ObjectiveWithKeyResultsSchema, category: PeriodCategory
) -> (int, int):
    now = datetime.now()
    if now.year - 1 != objective.year:
        return 0, 0

    if category == PeriodCategory.WEEK:
        if now.month == 1 and now.day < 8 and objective.achievement:
            return OBJECTIVE_WEIGHT, OBJECTIVE_WEIGHT
    elif category == PeriodCategory.MONTH:
        if now.month == 1 and objective.achievement:
            return OBJECTIVE_WEIGHT, OBJECTIVE_WEIGHT

    return 0, OBJECTIVE_WEIGHT


async def get_key_results_achievement_percent(
    key_results: List[KeyResultWithInitiativesSchema], category: PeriodCategory
) -> (float, int):
    achievement_scores = []
    now = datetime.now()
    if category == PeriodCategory.WEEK:
        current_time = time.mktime(now.date().timetuple())
        for key_result in key_results:
            due_time = time.mktime(key_result.due_date.timetuple())
            if due_time < current_time < due_time + 86400 * 8:
                achievement_scores.append(key_result.achievement_score)
    elif category == PeriodCategory.MONTH:
        current_month = now.year * 12 + now.month
        for key_result in key_results:
            due_month = key_result.due_date.year * 12 + key_result.due_date.month
            if due_month + 1 == current_month:
                achievement_scores.append(key_result.achievement_score)

    return (
        sum(achievement_scores) / KEY_RESULT_MAX_SCORE * KEY_RESULT_WEIGHT,
        len(achievement_scores) * KEY_RESULT_WEIGHT,
    )


# TODO 주요 행동 퍼센트 관련 작성 중
async def get_initiatives_achievement_percent(
    initiatives: List[InitiativeSchema], category: PeriodCategory
) -> (float, int):
    achievement_scores = []
    now = datetime.now()
    if category == PeriodCategory.WEEK:
        current_time = time.mktime(now.date().timetuple())
        for initiative in initiatives:
            open_time = time.mktime(initiative.open_date.timetuple())
            due_time = time.mktime(initiative.due_date.timetuple())
            last_done_date = initiative.done_times.get(str(initiative.current_metrics))
            if open_time < current_time < due_time + 86400 * 8:
                if not last_done_date:
                    achievement_scores.append(0)
                    continue
                done_date = datetime.strptime(last_done_date, "%Y-%m-%d %H:%M:%S.%f")
                if (
                    current_time - 86400 * 7
                    <= time.mktime(done_date.timetuple())
                    < current_time
                    or initiative.goal_metrics <= initiative.current_metrics
                ):
                    achievement_scores.append(INITIATIVE_WEIGHT)
                else:
                    achievement_scores.append(0)
    elif category == PeriodCategory.MONTH:
        pass

    return sum(achievement_scores), len(achievement_scores)
