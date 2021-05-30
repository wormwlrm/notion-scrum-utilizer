from main import scrum
from src.BurnChart import BurnChart


def run_create_burnchart():
    result = scrum.get_analysis_data_of_week()

    burn_chart = BurnChart(task_count=result["task_count"], data=result["data"])

    burn_chart.show()
