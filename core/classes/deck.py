from core.classes.card import Card
from core.classes.hand import Hand
from typing import List
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self) -> None:
        for suit in ["H", "D", "C", "S"]:
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "T",
                "J",
                "Q",
                "K",
                "A",
            ]:
                self.cards.append(Card(rank, suit))

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self, n=1) -> List[Card]:
        drawn = []
        for i in range(n):
            drawn.append(self.cards.pop())
        return drawn

    def draw_hand(self, n=1) -> Hand:
        # draw but as Hand object
        return Hand(self.draw(n))

    def size(self) -> int:
        return len(self.cards)

    def __len__(self):
        return self.size()

    def __str__(self):
        rstr = ""
        rstr += "Deck("
        for card in self.cards:
            rstr += str(card) + ", "
        rstr += "; size=" + str(len(self.cards)) + ")"
        return rstr

    def __repr__(self):
        return self.__str__()
