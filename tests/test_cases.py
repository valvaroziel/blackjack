from utils import classes
from utils import constants as con


def test_deck_is_full():
    deck = classes.Deck()

    assert deck.size() == 52

def test_deck_is_unique():
    deck = classes.Deck()
    deck_set = set(deck.cards)

    assert deck.size() == len(deck_set)

def test_deck_is_empty():
    deck = classes.Deck(empty=True)

    assert deck.size() == 0

def test_deck_is_shuffled():
    unshuffled_deck = classes.Deck()
    shuffled_deck = classes.Deck()
    shuffled_deck.shuffle_deck()

    print(shuffled_deck.fetch_cards())
    print()
    print(unshuffled_deck.fetch_cards())

    assert unshuffled_deck.fetch_cards() != shuffled_deck.fetch_cards()

def test_card_can_be_revealed():
    pass

def test_card_can_be_hidden():
    card = classes.Card(2, con.CLUBS)
    card.hide()

    assert card.fetch_data() == ('##', '###')

def test_card_can_generate_text():
    card = classes.Card(2, con.CLUBS)
    print()
    print(*card.generate_text(), sep='\n')

    assert card.generate_text() != None

def test_card_value_persists_after_being_hidden():
    card = classes.Card(2, con.CLUBS)
    card.hide()
    card.reveal()

    assert card.fetch_data() == ('2', con.CLUBS)