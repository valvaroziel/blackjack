from utils import classes
from utils import constants as con
from utils import helpers

class TestDeck:
    hand = [classes.Card('2', con.HEARTS), classes.Card('J', con.CLUBS), classes.Card('8', con.DIAMONDS)]

    def test_deck_is_full(self):
        deck = classes.Deck()

        assert deck.size() == 52

    def test_deck_is_unique(self):
        deck = classes.Deck()
        deck_set = set(deck.cards)

        assert deck.size() == len(deck_set)

    def test_deck_is_empty(self):
        deck = classes.Deck(empty=True)

        assert deck.size() == 0

    def test_deck_is_shuffled(self):
        unshuffled_deck = classes.Deck()
        shuffled_deck = classes.Deck()
        shuffled_deck.shuffle_deck()

        print(shuffled_deck.fetch_cards())
        print()
        print(unshuffled_deck.fetch_cards())

        assert unshuffled_deck.fetch_cards() != shuffled_deck.fetch_cards()

    def test_draw_removes_cards(self):
        deck = classes.Deck()
        initial_size = deck.size()
        deck.draw()

        assert deck.size() < initial_size

    def test_draw_returns_a_card(self):
        deck = classes.Deck()
        drawn_card: classes.Card = deck.draw()

        assert drawn_card

    def test_draw_adds_to_hand(self):
        deck = classes.Deck()
        deck.shuffle_deck()
        self.hand.append(deck.draw())

        for c in self.hand:
            print(c.fetch_data())

        assert len(self.hand) == 4


class TestCard:

    def test_card_can_be_revealed(self):
        card = classes.Card(2, con.CLUBS)
        card.hide()
        card.reveal()

        assert card.hidden is False

    def test_card_can_be_hidden(self):
        card = classes.Card(2, con.CLUBS)
        card.hide()

        assert card.fetch_data() == ('##', '###') and card.hidden is True

    def test_card_can_generate_text(self):
        card = classes.Card(2, con.CLUBS)
        print()
        print(*card.generate_text(), sep='\n')

        assert card.generate_text() != None

    def test_card_value_persists_after_being_hidden(self):
        card = classes.Card(2, con.CLUBS)
        card.hide()
        card.reveal()

        assert card.fetch_data() == ('2', con.CLUBS)

    def test_card_fetches_data_as_tuple(self):
        card = classes.Card(2, con.CLUBS)

        assert isinstance(card.fetch_data(), tuple)


class TestHelpers:
    hand = [classes.Card('2', con.HEARTS), classes.Card('J', con.CLUBS), classes.Card('8', con.DIAMONDS)]

    def test_hand_is_displayed(self):
        output = helpers.format_cards(self.hand)
        print()
        print(*output, sep='\n')

    def test_hand_can_be_totaled(self):
        assert helpers.value_hand(self.hand) == 20

    def test_ace_handling(self):
        ace_is_one = [classes.Card('2', con.HEARTS), classes.Card('J', con.CLUBS), classes.Card('8', con.DIAMONDS), classes.Card('A', con.HEARTS)]

        ace_is_eleven = [classes.Card('2', con.HEARTS), classes.Card('A', con.CLUBS), classes.Card('8', con.DIAMONDS)]

        assert helpers.value_hand(ace_is_one) and helpers.value_hand(ace_is_eleven) == 21

    def test_hitting(self):
        deck = classes.Deck()
        deck.shuffle_deck()
        self.hand.append(helpers.hit(deck))
        self.hand.append(helpers.hit(deck))
        self.hand.append(helpers.hit(deck))
        output = helpers.format_cards(self.hand)

        print()
        print(*output, sep='\n')
        print(f'\n{deck.size()}')

        assert deck.size() < 52 and len(self.hand) > 3

    def test_dealing(self):
        deck = classes.Deck(shuffled=True)
        hands = helpers.deal_cards(deck)
        dealer, player = hands

        assert (len(dealer) and len(player) == 2) and dealer[0].fetch_data() == ('##', '###')




