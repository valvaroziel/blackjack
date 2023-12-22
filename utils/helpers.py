from hmac import new
import constants
import classes

def format_cards(cards: list[classes.Card]) -> list[str, str, str, str, str]:
    """Takes a list of Card objects and formats them into a single list of strings ready to be unpacked and printed.

    Args:
        cards (list): A list containing the cards to be displayed as rows of strings.
    """

    output = ['','','','','']

    for card in cards:
        for i, raw in enumerate(card.generate_text()):
            output[i] += raw

    return output

def value_hand(cards: list[classes.Card]) -> int:
    """Returns the value of a set of cards according to blackjack rules.

    Args:
        cards (list[classes.Card]): The hand being evaluated.

    Returns:
        int: The total value o the hand.
    """

    hand = [card.fetch_data() for card in cards]     # Make a list of tuples containing the data from each card.
    total = 0

    for card in hand:
        # If it isn't a face card, add its value to the total
        if card[0] not in constants.FACES:
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

def hit(deck: classes.Deck) -> classes.Card:
    """Performs a 'hit' according to the rules of Blackjack.

    Args:
        deck (classes.Deck): The deck being played with.
    Returns:
        classes.Card: The card that the player drew.
    """
    new_card = deck.draw()

    return new_card

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

def bet(purse):
    print('Please enter a bet (or QUIT to stop playing)')
    user_input = input(f'(1-{purse} or QUIT): ')

    while user_input != 'QUIT' and isinstance(user_input, int) is False:
        user_input = input(f'Please input a number (1-{purse}) or type QUIT: ')

    return user_input

def action():
    pass
