from src.Slack import Slack


def run_send_to_slack():
    slack = Slack()
    slack.post_image("burnchart.png")


run_send_to_slack()
