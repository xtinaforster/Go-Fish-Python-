class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def print_card(self):
        print("{} of {}".format(self.rank, self.suit))
