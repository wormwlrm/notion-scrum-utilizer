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
        if (os.path.exists('.env')):
            load_dotenv(verbose=True)

        print('environ:', os.environ['TOKEN'])
        print('getenv:', os.getenv('TOKEN'))

        self.token = os.environ['TOKEN']
        self.client = NotionClient(token_v2=self.token)


