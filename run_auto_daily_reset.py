from main import scrum


def run_auto_daily_reset():
    key = scrum.conf["CARD"]["STATUS"]
    todo = scrum.conf["SCRUM"]["STEPS"]["TODO"]
    doing = scrum.conf["SCRUM"]["STEPS"]["DOING"]

    try:
        for card_id in scrum.get_filtered_card_ids(key, doing):
            card = scrum.client.get_block(card_id)
            setattr(card, key, todo)
        return True
    except:
        return False
