from blackjack import classes
from blackjack import constants


def test_deck_is_full():
    deck = classes.Deck

    assert len(deck) == 52
