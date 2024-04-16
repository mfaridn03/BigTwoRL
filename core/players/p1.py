from core.classes.card import Card
from core.classes.player import Player
from typing import List

from core.classes.utils import Utils


class Player1(Player):
    def __init__(self):
        # play lowest legal card
        super().__init__("Alice (lowest legal)")

    def play(self, game_data: dict) -> List[Card]:
        all_plays = Utils.get_all_valid_plays(self.hand, game_data)
        if len(all_plays) == 0:
            return []
        return [all_plays[0]]
