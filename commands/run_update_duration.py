from main import notion
from datetime import date
from notion.collection import NotionDate


def run_update_duration():
    update_done_card()
    update_doing_card()


def update_done_card():
    """
    DONE 상태의 카드의 DURATION을 새로 기록합니다.
    DURATION의 값이 없을 경우에는 시작일과 종료일을 모두 당일로 설정합니다.
    시작일이 존재할 때에는 종료일만 당일로 설정합니다.
    """
    key = notion.CARD_STATUS
    done = notion.DONE
    duration = notion.CARD_DURATION

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


def update_doing_card():
    """
    DOING 상태의 카드의 DURATION을 새로 기록합니다.
    DURATION의 값이 없을 경우에는 시작일을 당일로 설정합니다.
    """

    status = notion.CARD_STATUS
    doing = notion.DOING
    duration = notion.CARD_DURATION

    today = date.today()

    for card_id in notion.get_filtered_card_ids(status, doing):
        card = notion.client.get_block(card_id)

        notion_date = card.get_property(duration)
        if (not notion_date) or (notion_date.start == None):
            notion_date = NotionDate(start=today)

        card.set_property(duration, notion_date)
