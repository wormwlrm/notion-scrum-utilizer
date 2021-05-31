import os
from notion.client import NotionClient
from dotenv import load_dotenv
import pandas as pd

import utils
from src.Config import Config


class Notion(Config):
    client = None
    token = None
    board = None

    def __init__(self):
        super().__init__()
        self.set_token()
        self.set_scrum()

    def set_token(self):
        if os.path.exists(".env"):
            load_dotenv(verbose=True)

        self.token = os.environ["NOTION_TOKEN"]
        self.client = NotionClient(token_v2=self.token)

    def set_scrum(self):
        self.board = self.client.get_collection_view(self.SCRUM_URL)

    def get_filtered_card_ids(self, key, value):
        card_ids = []
        for card in self.board.collection.get_rows():
            current = self.client.get_block(card.id)

            if getattr(current, key) != value:
                continue

            card_ids.append(card.id)

        return card_ids

    def get_analysis_data_of_week(self):
        duration = self.CARD_DURATION
        status = self.CARD_STATUS
        done = self.DONE
        sprint_week = self.SPRINT_WEEK
        story_points_enabled = self.STORY_POINTS_ENABLED
        story_points = self.CARD_STORY_POINTS

        cards = self.board.collection.get_rows()

        if story_points_enabled:
            total_count = 0

            for card in cards:
                current_story_point = card.get_property(story_points)
                if current_story_point == None:
                    continue
                total_count += current_story_point
        else:
            total_count = len(cards)

        times = utils.get_time_series(
            start=utils.add_time(days=-sprint_week * 7), week=sprint_week
        )
        task_durations = [float(total_count) for _ in range(len(times))]

        for card in cards:
            if card.get_property(status) != done:
                continue

            notion_date = card.get_property(duration)

            # 해당 태스크 끝내는 데 걸린 시간
            task_duration = notion_date.end - notion_date.start

            if story_points_enabled:
                amount_of_task = card.get_property(story_points)
            else:
                amount_of_task = 1

            # 해당 태스크를 하루에 처리한 양
            task_per_day = float(amount_of_task / (task_duration.days + 1))

            duration_count = 0

            subtracting_start_date = notion_date.start + pd.Timedelta(days=1)
            subtracting_finish_date = notion_date.end + pd.Timedelta(days=1)

            for index, time in enumerate(times):
                if time < subtracting_start_date:
                    continue
                elif subtracting_start_date <= time <= subtracting_finish_date:
                    duration_count += 1
                    task_durations[index] = (
                        task_durations[index] - task_per_day * duration_count
                    )
                else:
                    task_durations[index] = (
                        task_durations[index] - task_per_day * duration_count
                    )

        return {"total_count": total_count, "data": task_durations}
