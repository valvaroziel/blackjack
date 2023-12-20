import random

import constants as con

class Card:
    def __init__(self, rank, suit, hidden=False) -> None:
        self.rank = str(rank)
        self.suit = suit
        self.hidden = hidden
        self.saved_values = None

        if self.hidden is True:
            self.rank = '##'
            self.suit = '###'

    def hide(self):
        self.saved_values = (self.rank, self.suit)

        self.rank = '##'
        self.suit = '###'
        self.hidden = True

    def reveal(self):
        self.rank = self.saved_values[0]
        self.suit = self.saved_values[1]
        self.hidden = False

    def generate_text(self):
        card_text = ['-------  ', f'|{self.rank:<5}|  ', f'|{self.suit:^5}|  ', f'|{self.rank:>5}|  ', '-------  ']

        return card_text

    def fetch_data(self) -> tuple[str,str]:
        """Returns a tuple containing a card's rank and suit.

        Returns:
            tuple: (rank, suit)
        """
        data = (self.rank, self.suit)

        return data

class Deck:
    def __init__(self, empty=False, shuffled=False):
        self.cards = []

        if empty is True:
            return

        for rank in range(13):
            for suit in range(4):
                self.cards.append(Card(con.RANKS[rank], con.SUITS[suit]))

        if shuffled is True:
            self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw(self):
        drawn_card = self.cards.pop()

        return drawn_card

    def size(self):
        return len(self.cards)

    def fetch_cards(self):
        card_data = []

        for card in self.cards:
            card_data.append(tuple((card.rank, card.suit)))

        return card_data