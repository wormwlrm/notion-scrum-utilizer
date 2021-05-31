from main import notion
from commands.run_weekly_archive import run_weekly_archive
from commands.run_weekly_backlog import run_weekly_backlog
from commands.run_create_burn_chart import run_create_burn_chart


if notion.WEEKLY_BURN_CHART:
    print("WEEKLY_BURN_CHART : ", run_create_burn_chart())

if notion.WEEKLY_ARCHIVE:
    print("WEEKLY_ARCHIVE : ", run_weekly_archive())

if notion.BACKLOG_ENABLED:
    print("BACKLOG_ENABLED : ", run_weekly_backlog())
