from main import scrum
from notion.collection import NotionDate
from datetime import date


def update_finished_time():
    key = scrum.conf['CARD']['STATUS']
    done = scrum.conf['SCRUM']['STEPS']['DONE']
    finished_at = scrum.conf['CARD']['FINISHED_AT']

    try:
        for card_id in scrum.get_filtered_card_ids(key, done):
            card = scrum.client.get_block(card_id)
            card.set_property(finished_at, NotionDate(date.today()))
        return True
    except:
        return False

