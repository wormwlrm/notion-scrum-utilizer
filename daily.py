from main import notion
from commands.run_auto_daily_reset import run_auto_daily_reset
from commands.run_auto_update_duration import run_auto_update_duration

if notion.AUTO_UPDATE_DURATION:
    print("AUTO_UPDATE_DURATION : ", run_auto_update_duration())

if notion.AUTO_DAILY_RESET:
    print("AUTO_DAILY_REST : ", run_auto_daily_reset())
