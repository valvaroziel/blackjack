class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    # def generate_text(self):
    #     if self.rank == 10:
    #         card_text = [' ------- \n', f'|{self.rank}   |\n', f'|  {self.suit}  |\n', f'|   {self.rank}|\n', '------- \n']
    #     else:
    #         card_text = [' -------  \n', f'|{self.rank:<5}|\n', f'|{self.suit:^5}|\n', f'|{self.rank:>5}|\n', '------- \n']


    #     return(card_text)
    def generate_text(self):
        card_text = ['-------  ', f'|{self.rank:<5}|  ', f'|{self.suit:^5}|  ', f'|{self.rank:>5}|  ', '-------  ']


        return(card_text)
