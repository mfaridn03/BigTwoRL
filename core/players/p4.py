from core.classes.card import Card
from core.classes.player import Player
from core.classes.utils import Utils
from typing import List

import random


class Player4(Player):
    def __init__(self):
        # random
        super().__init__("Dean (random)")
        self.low = True

    def play(self, game_data: dict) -> List[Card]:
        all_plays = Utils.get_all_valid_plays(self.hand, game_data)
        if len(all_plays) == 0:
            return []

        return [random.choice(all_plays)]
