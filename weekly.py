from main import scrum
from commands.run_auto_weekly_archive import run_auto_weekly_archive
from commands.run_create_burn_chart import run_create_burn_chart


if scrum.conf["OPTIONS"]["AUTO_WEEKLY_ARCHIVE"]:
    print("AUTO_WEEKLY_ARCHIVE : ", run_auto_weekly_archive())

if scrum.conf["OPTIONS"]["AUTO_WEEKLY_BURN_CHART"]:
    print("AUTO_WEEKLY_BURN_CHART : ", run_create_burn_chart())
