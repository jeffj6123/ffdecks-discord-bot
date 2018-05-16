import requests


class FFDecks:
    def __init__(self):
        self.cards = self.load_cards()

    def load_cards(self):
        all_cards_requests = requests.get('https://ffdecks.com/api/cards/basic')
        return all_cards_requests.json()

    def get_card_by_serial_number(self, serial_number):
        card = None
        for card_info in self.cards:
            if serial_number == card_info['serial_number']:
                card = card_info
        return card

    def get_cards_by_name(self, name):
        name = name.lower()
        possible_cards = []
        for card_info in self.cards:
            if name in card_info['name'].lower():
                possible_cards.append(card_info['name'] + ' - ' + card_info['serial_number'])

        return possible_cards

    def get_deck_by_url(self, url):
        deck_id = url[-16:]
        data = requests.get('https://ffdecks.com/api/deck?deck_id=' + deck_id)
        if data.status_code != 200:
            return None
        return data.json()

