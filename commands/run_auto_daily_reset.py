from main import notion


def run_auto_daily_reset():
    key = notion.CARD_STATUS
    todo = notion.TODO
    doing = notion.DOING

    try:
        for card_id in notion.get_filtered_card_ids(key, doing):
            card = notion.client.get_block(card_id)
            setattr(card, key, todo)
        return True
    except:
        return False
