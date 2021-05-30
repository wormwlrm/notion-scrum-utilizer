from main import scrum
from datetime import date
from notion.collection import NotionDate


def run_auto_update_duration():
    return update_done_card() and update_doing_card()


def update_done_card():
    key = scrum.conf["CARD"]["STATUS"]
    done = scrum.conf["SCRUM"]["STEPS"]["DONE"]
    duration = scrum.conf["CARD"]["DURATION"]

    try:
        today = date.today()

        for card_id in scrum.get_filtered_card_ids(key, done):
            card = scrum.client.get_block(card_id)
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
    status = scrum.conf["CARD"]["STATUS"]
    doing = scrum.conf["SCRUM"]["STEPS"]["DOING"]
    duration = scrum.conf["CARD"]["DURATION"]

    try:
        today = date.today()

        for card_id in scrum.get_filtered_card_ids(status, doing):
            card = scrum.client.get_block(card_id)

            notion_date = card.get_property(duration)
            if (not notion_date) or (notion_date.start == None):
                notion_date = NotionDate(start=today)

            card.set_property(duration, notion_date)
        return True
    except:
        return False
