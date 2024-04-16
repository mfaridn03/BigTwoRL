from core.classes.card import Card
from core.classes.player import Player
from typing import List

from core.classes.utils import Utils


class Player2(Player):
    def __init__(self):
        # play 2nd lowest legal card
        super().__init__("Bob (2nd lowest legal)")

    def play(self, game_data: dict) -> List[Card]:
        all_plays = Utils.get_all_valid_plays(self.hand, game_data)
        if len(all_plays) == 0:
            return []

        if len(all_plays) > 1:
            return [all_plays[1]]

        return [all_plays[0]]
