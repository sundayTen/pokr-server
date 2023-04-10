from datetime import datetime, timedelta

from fastapi_amis_admin.admin import AdminSite, Settings
from fastapi_scheduler import SchedulerAdmin

from crud.achievement_percent.create import create_achievement_percent
from crud.user.read import get_all_user
from db.config import get_db
from env import ACHIEVEMENT_PERCENT_SCHEDULING_HOUR, MISFIRE_GRACE_SECONDS
from schemas.achievement_percent import AchievementPercentSchema
from schemas.common import PeriodCategory
from service.metrics import calculate_achievement_percent

site = AdminSite(
    settings=Settings(database_url_async="sqlite+aiosqlite:///amisadmin.db")
)
scheduler = SchedulerAdmin.bind(site)


@scheduler.scheduled_job(
    "interval",
    hours=ACHIEVEMENT_PERCENT_SCHEDULING_HOUR,
    misfire_grace_time=MISFIRE_GRACE_SECONDS,
)
async def calculate_achievement_percent_weekly():
    now = datetime.now()
    if not now.weekday() and now.hour < ACHIEVEMENT_PERCENT_SCHEDULING_HOUR:
        db = next(get_db())
        percent, real_user_count = 0, 0
        time_for_calculating = now.today() - timedelta(days=7)
        month = time_for_calculating.month
        week = (time_for_calculating.day - 1) // 7 + 1
        users = await get_all_user(db)
        for user in users:
            current_percent = 0
            if user.objectives:
                current_percent = await calculate_achievement_percent(
                    user.objectives, PeriodCategory.WEEK
                )
                if current_percent:
                    percent += current_percent
                    real_user_count += 1

            await create_achievement_percent(
                AchievementPercentSchema(
                    user_id=user.id,
                    year=time_for_calculating.year,
                    category=PeriodCategory.WEEK,
                    label=f"{month}월 {week}주차",
                    percent=current_percent if current_percent else 0,
                ),
                db,
            )

        await create_achievement_percent(
            AchievementPercentSchema(
                year=time_for_calculating.year,
                category=PeriodCategory.WEEK,
                label=f"{month}월 {week}주차",
                percent=int(percent / real_user_count) if real_user_count else 0,
            ),
            db,
        )


@scheduler.scheduled_job(
    "interval",
    hours=ACHIEVEMENT_PERCENT_SCHEDULING_HOUR,
    misfire_grace_time=MISFIRE_GRACE_SECONDS,
)
async def calculate_achievement_percent_monthly():
    now = datetime.now()
    if now.day == 1 and now.hour < ACHIEVEMENT_PERCENT_SCHEDULING_HOUR:
        db = next(get_db())
        percent, real_user_count = 0, 0
        a_week_ago = now.today() - timedelta(days=7)
        users = await get_all_user(db)
        for user in users:
            current_percent = 0
            if user.objectives:
                current_percent = await calculate_achievement_percent(
                    user.objectives, PeriodCategory.MONTH
                )
                if current_percent:
                    percent += current_percent
                    real_user_count += 1

            await create_achievement_percent(
                AchievementPercentSchema(
                    user_id=user.id,
                    year=a_week_ago.year,
                    category=PeriodCategory.MONTH,
                    label=f"{a_week_ago.month}월",
                    percent=current_percent if current_percent else 0,
                ),
                db,
            )

        await create_achievement_percent(
            AchievementPercentSchema(
                year=a_week_ago.year,
                category=PeriodCategory.MONTH,
                label=f"{a_week_ago.month}월",
                percent=int(percent / real_user_count) if real_user_count else 0,
            ),
            db,
        )
