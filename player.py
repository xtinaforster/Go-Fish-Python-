class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    def print_hand(self):
        for card in self.hand:
            card.print_card()

    def check_hand(self, rank):
        for card in self.hand:
            if card.rank is rank:
                self.hand.remove(card)
                return card
        return ""
