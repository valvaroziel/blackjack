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
    for card in cards:
        if card.hidden is True:
            return '???'

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

def dealer_play(dealer, deck):
    if value_hand(dealer) < 17:
        dealer.append(hit(deck))

def deal_cards(deck: classes.Deck) -> list:
    """Initializes the dealer and player's hands.

    Args:
        deck (classes.Deck): The deck being used for the current game.

    Returns:
        list: Returns list with two nested lists, each one containing Card objects. Always in [dealer, player] order.
    """
    dealer = []
    player = []

    for _ in range(2):
        dealer.append(deck.draw())
        player.append(deck.draw())

    dealer[0].hide()

    return dealer, player

def wager(purse):
    print('Please enter a bet (or QUIT to stop playing)')
    user_input = input(f'(1-{purse} or QUIT): ')

    while str(user_input).upper() != 'QUIT' and user_input.isdigit() is False:
        user_input = input(f'Please input a number (1-{purse}) or type QUIT: ')

    return user_input

def action(dd=False, first=False):
    actions = ['H', 'S', 'D']

    if first is True:
        user_input = input('(H)it, (S)tand, (D)ouble down: ')

        while user_input.isdigit() or user_input.upper() not in actions:
            user_input = input('Input should be one of (H)it, (S)tand, (D)ouble down: ')
        return user_input.upper()

    actions.remove('D')

    if dd:
        actions.remove('S')

        user_input = input('You must (H)it, because you doubled down on your first turn: ')

        while user_input.isdigit() or user_input.upper() not in actions:
            user_input = input('Input must be (H)it: ')
        return user_input.upper()

    user_input = input('(H)it or (S)tand: ')

    while user_input.isdigit() or user_input.upper() not in actions:
        user_input = input('Input should be one of (H)it or (S)tand: ')

    return user_input.upper()

def check_state(dealer, player, move) -> dict or None:
    winner = {}
    dealer_score = value_hand(dealer)
    player_score = value_hand(player)

    # If neither player has a blackjack or has busted, there is no winner
    if player_score < 21 and dealer_score < 21:
        if move == 'S' and dealer_score >= 17:
            if dealer_score >= player_score:
                winner = {'dealer':dealer_score}
                return winner
            else:
                winner = {'player':player_score}
                return winner
        return winner

    # Check if either player has busted
    if player_score > 21 or dealer_score == 21:
        winner = {'dealer':dealer_score}
        return winner

    elif dealer_score > 21 or player_score == 21:
        winner = {'player':player_score}
        return winner

