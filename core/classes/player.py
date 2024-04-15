from core.classes.card import Card
from core.classes.hand import Hand
from typing import List


# Abstract class for a player
class Player:
    def __init__(self, name, hand: Hand = None):
        self.name = name
        self.hand = Hand() if hand is None else hand
        self.hand.sort()

    def play(self, cards: List[Card]) -> List[Card]:
        pass

    def has_card(self, card: Card) -> bool:
        pass

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()
