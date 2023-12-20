from utils import classes
#from blackjack import constants as con


def test_deck_is_full():
    deck = classes.Deck()

    assert deck.size() == 52
