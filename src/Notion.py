import os
from notion.client import NotionClient
from dotenv import load_dotenv
import yaml


class Notion:
    client = None
    token = None
    conf = None

    def __init__(self):
        self.set_config()
        self.set_token()

    def set_config(self):
        with open('config.yaml') as file:
            self.conf = yaml.load(file, Loader=yaml.BaseLoader)

    def set_token(self):
        load_dotenv(verbose=True)
        self.token = os.getenv('token_v2')
        self.client = NotionClient(token_v2=self.token)


