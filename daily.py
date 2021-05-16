from main import scrum
from run_auto_daily_reset import run_auto_daily_reset
from update_finished_time import update_finished_time

if scrum.conf['OPTIONS']['AUTO_DAILY_RESET']:
    print(run_auto_daily_reset())
    print(update_finished_time())
