import itertools
from typing import List

from core.classes.card import Card


class Utils:
    @staticmethod
    def is_valid_play(play: List[Card], data: dict) -> bool:
        # currently only support single card play
        if len(play) > 1:
            # print("Currently only support single card play.")
            return False

        # empty play
        # only allow if not the first play
        if len(play) == 0:
            # print("Empty play.")
            return len(data["play_to_beat"]) != 0

        # round start, must play 3D
        if data["round_start"]:
            # print("Round start, must play 3D.")
            return Card.lowest() in play

        # card not in hand
        for card in play:
            if card not in data["hand"]:
                # print("Card not in hand.")
                return False

        # same number of cards
        if len(play) != len(data["play_to_beat"]) and data["trick_start"] is False:
            # print("Invalid number of cards.")
            return False

        # higher card check
        if data["trick_start"] is False and play[0] < data["play_to_beat"][0]:
            # print("Card(s) not higher than current play.")
            return False

        return True

    @staticmethod
    def get_all_valid_plays(hand: List[Card], data: dict) -> List[Card]:
        # single card plays only
        # round start, play 3d
        if data["round_start"] and data["trick_start"]:
            return [Card.lowest()]

        # no play to beat (won last trick)
        if data["trick_start"]:
            return hand

        # get all valid plays
        valid_plays = []
        for card in hand:
            if card > data["play_to_beat"][0]:
                valid_plays.append(card)

        return valid_plays
