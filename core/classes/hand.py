from core.classes.card import Card
from typing import List
import random


# Hand: the collection of cards held by a player
class Hand(list):
    def __init__(self, cards: list = None):
        self.cards: List[Card] = cards if cards is not None else []

    def __str__(self):
        rstr = ""
        rstr += "Hand("
        for card in self.cards:
            rstr += str(card) + ", "
        rstr += "; size=" + str(len(self.cards)) + ")"
        return rstr

    def __repr__(self):
        return self.__str__()
