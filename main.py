import sys

from utils import classes, helpers, constants


def main():
    purse = constants.INITIAL_PURSE # Create the starting purse which is tracked between rounds.


    while True:     # Main program loop. Loops each time the user starts a new game; initializes the deck and player/dealer hands every time a round ends.
        deck = classes.Deck()
        deck.shuffle_deck()
        dealer, player = helpers.deal_cards(deck)
        bet = 0

        print(constants.RULES + '\n')
        print(f'Money: ${purse}')

        bet = helpers.bet(purse)
        if str(bet).upper() == 'QUIT':
            sys.exit()

        print(f'Bet: {bet}\n\n')
        while True:  # Turn loop. Every iteration of the outer loop is one game; every iteration of this loop is one turn of one game.
            print(f'DEALER: {helpers.value_hand(dealer)}')



if __name__ == "__main__":
    main()