from src.Notion import Notion

notion = Notion()


def get_filtered_card_ids(key, value):
    card_ids = []
    for card in notion.scrum.collection.get_rows():
        current = notion.client.get_block(card.id)

        if getattr(current, key) != value:
            continue

        card_ids.append(card.id)

    return card_ids


def run_auto_daily_reset():
    key = notion.conf['SCRUM']['STATUS']['NAME']
    todo = notion.conf['SCRUM']['STEPS']['TODO']
    doing = notion.conf['SCRUM']['STEPS']['DOING']

    for card_id in get_filtered_card_ids(key, doing):
        card = notion.client.get_block(card_id)
        setattr(card, key, todo)


if notion.conf['OPTIONS']['AUTO_DAILY_RESET']:
    print(run_auto_daily_reset())
