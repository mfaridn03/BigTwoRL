from core.classes.card import Card
from typing import List, Union


class Hand:
    def __init__(self, cards: List[Card] = None):
        self.cards = cards if cards is not None else []

    def sort(self) -> None:
        self.cards.sort()

    def remove(self, card: Union[Card, List[Card]]) -> None:
        if isinstance(card, list):
            for c in card:
                self.cards.remove(c)
        else:
            self.cards.remove(card)

    def highs(self) -> List[Card]:
        return [c for c in self.cards if c.is_high()]

    def lows(self) -> List[Card]:
        return [c for c in self.cards if c.is_low()]

    def is_empty(self) -> bool:
        return len(self.cards) == 0

    def __str__(self):
        return f"{self.cards}"

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, item):
        return self.cards[item]
