from main import notion, slack
from src.BurnChart import BurnChart


def run_send_to_slack():
    slack.post_image("burnchart.png")


def run_create_burn_chart():
    result = notion.get_analysis_data_of_week()

    burn_chart = BurnChart()

    burn_chart.create_image(task_count=result["task_count"], data=result["data"])

    run_send_to_slack()
