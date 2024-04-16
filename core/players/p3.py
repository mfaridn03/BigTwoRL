from core.classes.card import Card
from core.classes.player import Player
from typing import List

from core.classes.utils import Utils


class Player3(Player):
    def __init__(self):
        # try to equalise low and high cards
        super().__init__("Christine (equalise)")

    def play(self, game_data: dict) -> List[Card]:
        valid = Utils.get_all_valid_plays(self.hand, game_data)

        if len(valid) == 0:
            return []
        if len(valid) == 1:
            return [valid[0]]

        # otherwise, play the card that will equalise the number of high and low cards
        if len(self.hand.highs()) > len(self.hand.lows()):
            h = [c for c in valid if c.is_low()]
            if h:
                return [h[0]]
            return [valid[0]]

        l = [c for c in valid if c.is_high()]
        if l:
            return [l[0]]
        return [valid[0]]
