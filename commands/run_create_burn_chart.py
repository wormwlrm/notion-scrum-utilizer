from main import notion, slack
from src.BurnChart import BurnChart
from src.Slack import Slack


def run_send_to_slack():
    slack.post_image("burnchart.png")


def run_create_burnchart():
    result = notion.get_analysis_data_of_week()

    burn_chart = BurnChart(task_count=result["task_count"], data=result["data"])

    burn_chart.save_image()

    run_send_to_slack()
