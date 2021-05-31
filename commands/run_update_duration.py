from main import notion
from datetime import date
from notion.collection import NotionDate


def run_update_duration():
    return update_done_card() and update_doing_card()


def update_done_card():
    key = notion.CARD_STATUS
    done = notion.DONE
    duration = notion.CARD_DURATION

    try:
        today = date.today()

        for card_id in notion.get_filtered_card_ids(key, done):
            card = notion.client.get_block(card_id)
            notion_date = card.get_property(duration)

            if not notion_date:
                notion_date = NotionDate(start=today, end=today)

            if notion_date.start == None:
                notion_date = NotionDate(start=today)

            if notion_date.end == None:
                notion_date = NotionDate(start=notion_date.start, end=today)

            card.set_property(duration, notion_date)
        return True
    except:
        return False


def update_doing_card():
    status = notion.CARD_STATUS
    doing = notion.DOING
    duration = notion.CARD_DURATION

    try:
        today = date.today()

        for card_id in notion.get_filtered_card_ids(status, doing):
            card = notion.client.get_block(card_id)

            notion_date = card.get_property(duration)
            if (not notion_date) or (notion_date.start == None):
                notion_date = NotionDate(start=today)

            card.set_property(duration, notion_date)
        return True
    except:
        return False
