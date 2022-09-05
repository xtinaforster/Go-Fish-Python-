from gofish import GoFish


def main():
    game = GoFish()
    game.setup(4)
    while game.playing:
        game.turn(4)
    winner = game.players[0]
    for player in game.players:
        if winner.score < player.score:
            winner = player
    print('The winner is {} with {} matches'.format(winner.name, winner.score))


main()
