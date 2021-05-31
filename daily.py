from main import notion
from commands.run_daily_reset import run_daily_reset
from commands.run_update_duration import run_update_duration

if notion.UPDATE_DURATION:
    print("UPDATE_DURATION : ", run_update_duration())

if notion.DAILY_RESET:
    print("DAILY_REST : ", run_daily_reset())
