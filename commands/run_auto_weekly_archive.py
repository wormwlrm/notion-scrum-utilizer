from main import scrum


def run_auto_weekly_archive():
    key = scrum.conf["CARD"]["STATUS"]
    done = scrum.conf["SCRUM"]["STEPS"]["DONE"]
    archive = scrum.conf["SCRUM"]["STEPS"]["ARCHIVE"]

    try:
        for card_id in scrum.get_filtered_card_ids(key, done):
            card = scrum.client.get_block(card_id)
            setattr(card, key, archive)
        return True
    except:
        return False
