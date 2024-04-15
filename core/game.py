from core.classes.deck import Deck
from core.classes.player import Player


class Game:
    def __init__(self):
        self.data = {}
        self.players = [
            Player("Alice"),
            Player("Bob"),
            Player("Charlie"),
            Player("David"),
        ]

    def init(self):
        deck = Deck()
        deck.shuffle()

        # give 16 to each player
        for player in self.players:
            player.hand = deck.draw(13)
            player.hand.sort()

        # whoever has 3D goes first
        for player in self.players:
            if player.hand.has_card("3", "D"):
                self.players.remove(player)
                self.players.insert(0, player)
                break

        print("Order: ", [player.name for player in self.players])

    def start(self):
        self.init()
        for player in self.players:
            print(f"{player}: {player.hand}")
