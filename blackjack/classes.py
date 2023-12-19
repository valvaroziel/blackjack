import random

import constants as con

class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit
        self.flipped = False

    def hide_card(self):
        self.rank = '##'
        self.suit = '###'

    def generate_text(self):
        card_text = ['-------  ', f'|{self.rank:<5}|  ', f'|{self.suit:^5}|  ', f'|{self.rank:>5}|  ', '-------  ']

        return card_text

class Deck:
    def __init__(self):
        cards = []

        for rank in range(13):
            for suit in range(4):
                cards.append(Card(rank, con.SUITS[suit]))
