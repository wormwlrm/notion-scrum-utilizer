import os
from dotenv import load_dotenv
import yaml
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from Config import Config


class Slack(Config):
    token = None
    conf = None
    client = None

    def __init__(self):
        super().__init__()
        self.set_token()

    def set_token(self):
        if os.path.exists(".env"):
            load_dotenv(verbose=True)

        self.token = os.environ["SLACK_TOKEN"]
        self.client = WebClient(token=self.token)

    def post_image(self, file):
        channel_name = self.SLACK_CHANNEL_NAME

        try:
            response = self.client.files_upload(
                channels=channel_name,
                file=file,
            )
            assert response.data["ok"] is True
        except SlackApiError as e:
            print(f"{e.response['error']}")
