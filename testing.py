from core.classes.card import Card
from core.classes.deck import Deck
from core.classes.player import Player
from core.game import Game


def test():
    deck = Deck()

    # create player
    player = Player("Alice", deck.draw(13))
    print(player.hand)

    # card comparisons
    lowest = Card("4", "H")
    lower = Card("5", "D")
    higher = Card("T", "S")
    highest = Card("A", "C")

    print(f"lowest < lower: {lowest < lower}")
    print(f"lower < higher: {lower < higher}")
    print(f"higher > highest: {higher > highest}")
    print(f"highest < lowest: {highest < lowest}")


if __name__ == "__main__":
    # test()
    game = Game()
    game.start()
