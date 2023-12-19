import random

import constants as con

class Card:
    def __init__(self, rank, suit, hidden=False) -> None:
        self.rank = rank
        self.suit = suit
        self.hidden = hidden
        self.saved_values = None

    def hide_card(self):
        self.saved_values = (self.rank, self.suit)

        self.rank = '##'
        self.suit = '###'
        self.hidden = True

    def reveal_card(self):
        self.rank = self.saved_values[0]
        self.suit = self.saved_values[1]
        self.hidden = False

    def generate_text(self):
        card_text = ['-------  ', f'|{self.rank:<5}|  ', f'|{self.suit:^5}|  ', f'|{self.rank:>5}|  ', '-------  ']

        return card_text

class Deck:
    def __init__(self):
        cards = []

        for rank in range(13):
            for suit in range(4):
                cards.append(Card(rank, con.SUITS[suit]))

        self.shuffle_deck()

    def shuffle_deck(self):
        pass

    def draw(self):
        pass