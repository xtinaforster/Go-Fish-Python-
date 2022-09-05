from card import Card
import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]


class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in range(1, 13):
                self.cards.append(Card(suit, rank))

    def print_deck(self):
        for card in self.cards:
            card.print_card()

    def shuffle(self):
        for i in range(len(self.cards) - 1):
            temp = self.cards[i]
            num = random.randint(i + 1, len(self.cards) - 1)
            self.cards[i] = self.cards[num]
            self.cards[num] = temp

    def deal_card(self, player):
        if len(self.cards) > 0:
            card = random.choice(self.cards)
            player.hand.append(card)
            self.cards.remove(card)
        else:
            print("Out Of Cards!")
