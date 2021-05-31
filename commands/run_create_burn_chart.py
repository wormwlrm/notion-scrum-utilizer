from main import notion, slack
from src.BurnChart import BurnChart


def send_image_to_slack():
    """
    등록한 슬랙 채널로 번다운, 번업 차트 이미지를 전송합니다.
    """
    slack.post_image("burnchart.png")


def create_burn_chart():
    """
    CONFIG 파일에서 설정한 옵션과 노션의 태스크 카드에 기록된 진행 사항을 바탕으로
    번다운 또는 번업 이미지를 생성합니다.
    """
    direction = notion.BURN_CHART_TYPE
    y_label = "Story Points" if notion.STORY_POINTS_ENABLED else "Task Counts"

    result = notion.get_analysis_data_of_week(direction=direction)

    burn_chart = BurnChart()
    burn_chart.create_image(
        total_count=result["total_count"],
        data=result["data"],
        y_label=y_label,
        direction=direction,
    )


def run_create_burn_chart():
    create_burn_chart()
    send_image_to_slack()
