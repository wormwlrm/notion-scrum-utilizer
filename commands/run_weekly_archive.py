from main import notion
from commands.run_update_status import run_update_status


def run_weekly_archive():
    key = notion.CARD_STATUS
    done = notion.DONE
    archive = notion.ARCHIVE

    return run_update_status(key, done, archive)
