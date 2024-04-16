from core.classes.card import Card
from core.classes.hand import Hand
from typing import List


class Player:
    def __init__(self, name):
        self.name: str = name
        self.hand: Hand = Hand()
        self.hand.sort()
        self.id = -1  # this will be determined by the game
        # TEMP
        self.wins = 0

    def play(self, game_data: dict) -> List[Card]:
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
