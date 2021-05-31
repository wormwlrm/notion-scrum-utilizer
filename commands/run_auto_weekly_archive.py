from main import notion


def run_auto_weekly_archive():
    key = notion.CARD_STATUS
    done = notion.DONE
    archive = notion.ARCHIVE

    try:
        for card_id in notion.get_filtered_card_ids(key, done):
            card = notion.client.get_block(card_id)
            setattr(card, key, archive)
        return True
    except:
        return False
