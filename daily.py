from main import scrum
from run_auto_daily_reset import run_auto_daily_reset
from run_auto_update_duration import run_auto_update_duration

if scrum.conf["OPTIONS"]["AUTO_UPDATE_DURATION"]:
    print("AUTO_UPDATE_DURATION : ", run_auto_update_duration())

if scrum.conf["OPTIONS"]["AUTO_DAILY_RESET"]:
    print("AUTO_DAILY_REST : ", run_auto_daily_reset())
