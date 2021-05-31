from main import notion


def run_update_status(key, before, after):
    try:
        for card_id in notion.get_filtered_card_ids(key, before):
            card = notion.client.get_block(card_id)
            setattr(card, key, after)
        return True
    except:
        return False
