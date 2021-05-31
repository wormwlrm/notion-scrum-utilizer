from main import notion
from commands.run_update_status import run_update_status


def run_daily_reset():
    """
    STATUS가 DOING인 카드를 TODO로 옮깁니다.
    """
    key = notion.CARD_STATUS
    doing = notion.DOING
    todo = notion.TODO

    return run_update_status(key, doing, todo)
