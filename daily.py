from main import scrum
from run_auto_daily_reset import run_auto_daily_reset
from run_auto_update_duration import run_auto_update_duration

if scrum.conf['OPTIONS']['AUTO_DAILY_RESET']:
    print(run_auto_daily_reset())

if scrum.conf['OPTIONS']['AUTO_UPDATE_DURATION']:
    print(run_auto_update_duration())

