from src.Notion import Notion


class Scrum(Notion):
    board = None

    def __init__(self):
        super().__init__()
        self.set_scrum()

    def set_scrum(self):
        url = self.conf["SCRUM"]["URL"]
        self.board = self.client.get_collection_view(url)

    def get_filtered_card_ids(self, key, value):
        card_ids = []
        for card in self.board.collection.get_rows():
            current = self.client.get_block(card.id)

            if getattr(current, key) != value:
                continue

            card_ids.append(card.id)

        return card_ids
