from deck import Deck
from player import Player
import os
import time

clearConsole = lambda: os.system('cls'
                                 if os.name in ('nt', 'dos') else 'clear')


class GoFish:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.playing = True

    def setup(self, num_of_player):
        self.deck = Deck()
        self.deck.shuffle()
        for player_num in range(num_of_player):
            self.players.append(Player("Player " + str(player_num)))
            player = self.players[player_num]
            if num_of_player <= 3:
                for card in range(7):
                    self.deck.deal_card(player)
            else:
                for card in range(5):
                    self.deck.deal_card(player)

    def turn(self, num_of_players):
        for player in self.players:
            print("{}'s Turn".format(player.name))
            player.print_hand()
            chosen_card = int(
                input("What Card Do You Want To Ask For? (1-13)"))
            while chosen_card > 13 or chosen_card < 1:
                clearConsole()
                chosen_card = int(
                    input("What Card Do You Want To Ask For? (1-13)"))
            player_num = int(input("Which Player Are You Asking a Card For?"))
            while player_num > num_of_players - 1 or player_num < 0 or self.players[
                    player_num] is player:
                clearConsole()
                player_num = int(
                    input("Which Player Are You Asking a Card For?"))
            correct_card = self.players[player_num].check_hand(chosen_card)
            if chosen_card != "":
                clearConsole()
                print("Dang! Here is the Card you are looking for: {}".format(
                    chosen_card))
                player.hand.append(correct_card)
            else:
                clearConsole()
                print("Go Fish!")
                self.deck.deal_card(player)
            player.print_hand()
            time.sleep(1)
            clearConsole()
