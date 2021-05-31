from main import notion
from commands.run_update_status import run_update_status


def run_weekly_backlog():
    """
    STATUS가 BACKLOG인 카드를 TODO로 옮깁니다.
    """
    key = notion.CARD_STATUS
    backlog = notion.BACKLOG
    todo = notion.TODO

    return run_update_status(key, backlog, todo)
