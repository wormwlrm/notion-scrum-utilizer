import yaml
from utils import str_to_bool


class Config:
    def __init__(self):
        self.set_config()

    def set_config(self):
        with open("config.yaml") as file:
            conf = yaml.load(file, Loader=yaml.BaseLoader)

            self.set_scrum_config(conf["SCRUM"])
            self.set_card_config(conf["CARD"])
            self.set_options_config(conf["OPTIONS"])
            self.set_slack_config(conf["SLACK"])

    def set_scrum_config(self, scrum):
        self.SCRUM_URL = scrum["URL"]
        self.SPRINT_WEEK = int(scrum["SPRINT_WEEK"])
        self.BACKLOG = scrum["STEPS"]["BACKLOG"]
        self.TODO = scrum["STEPS"]["TODO"]
        self.DOING = scrum["STEPS"]["DOING"]
        self.DONE = scrum["STEPS"]["DONE"]
        self.ARCHIVE = scrum["STEPS"]["ARCHIVE"]

    def set_card_config(self, card):
        self.CARD_STATUS = card["STATUS"]
        self.CARD_DURATION = card["DURATION"]
        self.CARD_STORY_POINTS = card["STORY_POINTS"]

    def set_options_config(self, options):
        self.BACKLOG_ENABLED = str_to_bool(options["BACKLOG_ENABLED"])
        self.WEEKLY_ARCHIVE = str_to_bool(options["WEEKLY_ARCHIVE"])
        self.DAILY_RESET = str_to_bool(options["DAILY_RESET"])
        self.UPDATE_DURATION = str_to_bool(options["UPDATE_DURATION"])
        self.WEEKLY_BURN_CHART = str_to_bool(options["WEEKLY_BURN_CHART"])
        self.STORY_POINTS_ENABLED = str_to_bool(options["STORY_POINTS_ENABLED"])
        self.BURN_CHART_TYPE = options["BURN_CHART_TYPE"]

    def set_slack_config(self, slack):
        self.SLACK_CHANNEL_NAME = slack["CHANNEL_NAME"]
