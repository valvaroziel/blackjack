import constants
import classes

def format_cards(cards: list[classes.Card]):
    """Takes a list of Card objects and formats them into a single list of strings ready to be unpacked and printed.

    Args:
        cards (list): A list containing the cards to be displayed.
    """
    output = ['','','','','']

    for card in cards:
        for i, raw in enumerate(card.generate_text()):
            output[i] += raw

    return output

def value_hand(cards: list[classes.Card]):
    hand = [card.fetch_data() for card in cards]
    faces = constants.FACES
    total = 0

    for card in hand:
        # If it isn't a face card, add its value to the total
        if card[0] not in faces:
            total += int(card[0])
            continue
        # If it's a non-Ace face card, add 10 to the total
        elif card[0] != 'A':
            total += 10
            continue

        # Ace handling: 11 if it won't cause a bust, 1 otherwise
        if total <= 10:
            total += 11
        else:
            total += 1

    return total

def hit(cards: list[classes.Card], deck: classes.Deck):
    cards.append(deck.draw())

def stand():
    pass

def double_down():
    pass


def deal_cards(deck: classes.Deck):
    dealer = []
    player = []

    for _ in range(2):
        dealer.append(deck.draw())
        player.append(deck.draw())

    dealer[0].hide()

    return dealer, player
