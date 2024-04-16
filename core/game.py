from typing import List
from core.classes.card import Card
from core.classes.deck import Deck
from core.classes.hand import Hand
from core.classes.player import Player
from core.classes.utils import Utils


class Game:
    def __init__(self):
        self.players = [
            Player("Alice"),
            Player("Bob"),
            Player("Christine"),
            Player("Dean"),
        ]
        self.ci: int = 0
        self.trick_start: bool = True
        self.round_start: bool = True

        # play data
        self.play_to_beat: List[Card] = []
        self.round_history: List[List[Card]] = []
        self.hand_sizes: List[int] = [13, 13, 13, 13]

        # game data
        self.scores: List[int] = [0, 0, 0, 0]
        self.round_no: int = 0

        # other
        self._passes: int = 0

    def game_loop(self):
        while self.round_loop():
            pass

        self.round_start = True

        # loop until 10 rounds

    def round_loop(self):
        while self.trick_loop():
            pass

        self.play_to_beat = []
        self.trick_start = True
        print("Trick ends, winner: ", self.players[self.ci].name)
        print("------------")

        # check if any player has no cards left
        for _, player in enumerate(self.players):
            if len(player.hand) == 0:
                print(f"{player.name} has no cards left. GG")
                self.scores[player.id] += 1
                return False

        return True

    def trick_loop(self):
        print(f"\n{self.players[self.ci].name}'s turn")
        print("Your hand: ", self.players[self.ci].hand)
        print("To beat:", self.play_to_beat)

        # get play from player
        play = self.get_play_loop()

        # stop if player has no cards left
        if self.players[self.ci].hand.is_empty():
            return False

        # player passed
        if play == []:
            self._passes += 1
        else:
            self._passes = 0
            self.play_to_beat = play.copy()

        self.ci = (self.ci + 1) % 4
        self.trick_start = False
        self.round_start = False

        # 3 passes = trick ends
        if self._passes == 3:
            self._passes = 0
            return False
        else:
            return True

    def get_play_loop(self):
        while True:
            try:
                cards = input("Enter cards: ").upper().split()
                to_play = []

                # handle pass
                if "PASS" in cards and Utils.is_valid_play([], self.get_data()):
                    return []

                for card in cards:
                    card = Card.from_str(card)
                    to_play.append(card)

                # check if cards are valid
                if Utils.is_valid_play(to_play, self.get_data()):
                    # remove cards
                    for card in to_play:
                        self.players[self.ci].hand.remove(card)

                    return to_play

            except (ValueError, IndexError):
                pass

    def get_data(self) -> dict:
        """
        * `hand`: A list of card strings that are the card(s) in your hand.
        * `play_to_beat`: The current best play of the trick. If no such play exists (you are the first play in the trick), this will be an empty list.
        * `round_history`: A list of *trick_history* entries.
          A *trick_history* entry is a list of *trick_play* entries.
          Each *trick_play* entry is a `(player_no, play)` 2-tuple, where `player_no` is an integer between 0 and 3 (inclusive) indicating which player made the play, and `play` is the play that said player made, which will be a list of card strings.
        * `player_no`: An integer between 0 and 3 (inclusive) indicating which player number you are in the game.
        * `hand_sizes`: A 4-tuple of integers representing the number of cards each player has in their hand, in player number order.
        * `scores`: A 4-tuple of integers representing the score of each player at the start of this round, in player number order.
        * `round_no`: An integer between 0 and 9 (inclusive) indicating which round number is currently being played.
        """
        return {
            "hand": self.players[self.ci].hand,
            "play_to_beat": self.play_to_beat,
            "trick_start": self.trick_start,  # start of trick or not
            "round_start": self.round_start,  # start of round or not
            "round_history": self.round_history,
            "hand_sizes": self.hand_sizes,
            "scores": self.scores,
        }

    def reset(self):
        self.ci = 0
        self.trick_start = True
        self.round_start = True

        self.play_to_beat = []
        self.round_history = []
        self.hand_sizes = [13, 13, 13, 13]
        self.scores = [0, 0, 0, 0]

    def init(self):
        self.reset()

        deck = Deck()
        deck.shuffle()

        # give 16 to each player
        for i, player in enumerate(self.players):
            player.hand = Hand(deck.draw(13))
            player.hand.sort()
            player.id = i

        # whoever has 3D goes first
        # shift players list until 3D owner is at index 0
        while self.players[0].hand[0] != Card.lowest():
            self.players.append(self.players.pop(0))

        self.game_loop()

    def start(self):
        self.init()
