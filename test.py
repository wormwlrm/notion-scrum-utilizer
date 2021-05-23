from main import scrum
from run_auto_update_duration import run_auto_update_duration

if scrum.conf['OPTIONS']['AUTO_UPDATE_DURATION']:
    print(run_auto_update_duration())

