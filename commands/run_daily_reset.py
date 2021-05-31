from main import notion
from commands.run_update_status import run_update_status


def run_daily_reset():
    key = notion.CARD_STATUS
    todo = notion.TODO
    doing = notion.DOING

    return run_update_status(key, todo, doing)
