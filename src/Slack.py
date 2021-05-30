import os
from dotenv import load_dotenv
import yaml
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class Slack:
    token = None
    conf = None
    client = None

    def __init__(self):
        self.set_config()
        self.set_token()

    def set_config(self):
        with open("config.yaml") as file:
            self.conf = yaml.load(file, Loader=yaml.BaseLoader)

    def set_token(self):
        if os.path.exists(".env"):
            load_dotenv(verbose=True)

        self.token = os.environ["SLACK_TOKEN"]
        self.client = WebClient(token=self.token)

    def post_image(self, file):
        channel_name = self.conf["SLACK"]["CHANNEL_NAME"]

        try:
            response = self.client.files_upload(
                channels=channel_name,
                file=file,
            )
            assert response.data["ok"] is True
        except SlackApiError as e:
            print(f"{e.response['error']}")
