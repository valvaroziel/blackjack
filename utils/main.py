import sys

# from utils import classes, helpers, constants
import classes, helpers, constants


def main():
    purse = constants.INITIAL_PURSE # Create the starting purse which is tracked between rounds.
    print(constants.RULES + '\n')

    while True:     # Main program loop. Loops each time the user starts a new game; initializes the deck and player/dealer hands every time a round ends.
        deck = classes.Deck()
        deck.shuffle_deck()
        dealer, player = helpers.deal_cards(deck)
        bet = 0
        turn = 1
        # is_standing = False
        doubled_down = False
        move = ''
        winner = None

        print(f'Money: ${purse}')

        bet = helpers.wager(purse)
        if str(bet).upper() == 'QUIT':
            sys.exit()
        bet = int(bet)
        # hands = [dealer, player]
        print(f'Bet: {bet}\n')

        while True:  # Turn loop. Every iteration of the outer loop is one game; every iteration of this loop is one turn of one game.
            print(f'DEALER: {helpers.value_hand(dealer)}')
            print(*helpers.format_cards(dealer), sep='\n')
            print()
            print(f'YOU: {helpers.value_hand(player)}')
            print(*helpers.format_cards(player), sep='\n')

            if turn == 1 and helpers.value_hand(player) == 21:
                winner = {'player':21}

            if winner:
                winner = list(winner.items())
                winner = winner[0]

                if winner[0] == 'dealer':
                    print('The House wins!')
                    purse = purse - bet
                    break

                print(f'\nYou won ${bet}!\n')
                purse += bet
                break

            if move != 'S':
                move = helpers.action(first=True) if turn == 1 else helpers.action(dd=doubled_down)

            if move == 'H':
                if doubled_down:
                    doubled_down = False
                player.append(helpers.hit(deck))
                print(f'You drew a {player[-1].rank} of {player[-1].suit}')
            elif move == 'D':
                bet *= 2
                print(f'You\'ve doubled your wager to {bet}, but must (H)it next turn.')
                doubled_down = 1

            if turn == 1:
                dealer[0].reveal()

            helpers.dealer_play(dealer, deck)
            winner = helpers.check_state(dealer, player, move)

            turn += 1\


if __name__ == "__main__":
    main()