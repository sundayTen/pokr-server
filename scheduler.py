from datetime import datetime

from fastapi_amis_admin.admin import AdminSite, Settings
from fastapi_scheduler import SchedulerAdmin

from crud.user.read import get_all_user
from db.config import get_db
from env import ACHIEVEMENT_PERCENT_SCHEDULING_HOUR
from schemas.common import PeriodCategory
from service.metrics import calculate_achievement_percent

site = AdminSite(
    settings=Settings(database_url_async="sqlite+aiosqlite:///amisadmin.db")
)
scheduler = SchedulerAdmin.bind(site)


@scheduler.scheduled_job("interval", seconds=1000)
async def calculate_achievement_percent_weekly():
    db = next(get_db())
    percent, real_user_count = 0, 0
    users = await get_all_user(db)
    for user in users:
        if user.objectives:
            percent += await calculate_achievement_percent(
                user.objectives, PeriodCategory.WEEK
            )
            real_user_count += 1

    print(f"전체 유저 달성률: {int(percent / real_user_count)}")


@scheduler.scheduled_job("interval", hours=ACHIEVEMENT_PERCENT_SCHEDULING_HOUR)
async def calculate_achievement_percent_weekly():
    now = datetime.now()
    if not now.weekday() and now.hour < ACHIEVEMENT_PERCENT_SCHEDULING_HOUR:
        db = next(get_db())
        percent, real_user_count = 0, 0
        users = await get_all_user(db)
        for user in users:
            if user.objectives:
                percent += await calculate_achievement_percent(
                    user.objectives, PeriodCategory.WEEK
                )
                real_user_count += 1

        print(int(percent / real_user_count))


@scheduler.scheduled_job("interval", hours=ACHIEVEMENT_PERCENT_SCHEDULING_HOUR)
async def calculate_achievement_percent_monthly():
    now = datetime.now()
    if now.day == 1 and now.hour < ACHIEVEMENT_PERCENT_SCHEDULING_HOUR:
        print("계산 중...")
