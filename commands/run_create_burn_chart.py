from main import notion, slack
from src.BurnChart import BurnChart


def run_send_to_slack():
    slack.post_image("burnchart.png")


def run_create_burn_chart():
    result = notion.get_analysis_data_of_week()

    burn_chart = BurnChart()

    y_label = "Story Points" if notion.STORY_POINTS_ENABLED else "Task Count"

    burn_chart.create_image(
        total_count=result["total_count"], data=result["data"], y_label=y_label
    )

    run_send_to_slack()
