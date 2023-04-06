from datetime import datetime

from fastapi_amis_admin.admin import AdminSite, Settings
from fastapi_scheduler import SchedulerAdmin

from env import ACHIEVEMENT_PERCENT_SCHEDULING_HOUR

site = AdminSite(
    settings=Settings(database_url_async="sqlite+aiosqlite:///amisadmin.db")
)
scheduler = SchedulerAdmin.bind(site)


@scheduler.scheduled_job("interval", hours=ACHIEVEMENT_PERCENT_SCHEDULING_HOUR)
async def calculate_achievement_percent_weekly():
    now = datetime.now()
    if not now.weekday() and now.hour < ACHIEVEMENT_PERCENT_SCHEDULING_HOUR:
        print("계산 중...")


@scheduler.scheduled_job("interval", hours=ACHIEVEMENT_PERCENT_SCHEDULING_HOUR)
async def calculate_achievement_percent_monthly():
    now = datetime.now()
    if now.day == 1 and now.hour < ACHIEVEMENT_PERCENT_SCHEDULING_HOUR:
        print("계산 중...")
