from typing import List, Tuple
from core.classes.card import Card
from core.classes.deck import Deck
from core.classes.hand import Hand
from core.classes.player import Player
from core.classes.utils import Utils

# players
from core.players.p1 import Player1
from core.players.p2 import Player2
from core.players.p3 import Player3
from core.players.p4 import Player4


class GameAuto:
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.players: List[Player] = [
            Player1(),
            Player2(),
            Player3(),
            Player4(),
        ]
        self.ci: int = 0
        self.trick_start: bool = True
        self.round_start: bool = True

        # play data
        self.play_to_beat: List[Card] = []
        self.round_history: List[List[Tuple[int, str]]] = []
        self.hand_sizes: List[int] = [13, 13, 13, 13]

        # game data
        self.scores: List[int] = [0, 0, 0, 0]
        self.round_no: int = 1

        # other
        self._passes: int = 0
        self.ROUND_LIMIT = 10

    def game_loop(self):
        for i in range(self.ROUND_LIMIT):
            self.init()
            self.round_no = i + 1

            while self.round_loop():
                pass

            # reset round
            self.round_start = True

    def round_loop(self):
        """
        Stuff that's done in a round
        """
        # update round history
        self.round_history.append([])

        while self.trick_loop():
            # time.sleep(0.1)
            pass

        # reset trick
        self.play_to_beat = []
        self.trick_start = True

        if self.verbose:
            print(f"Trick ends, winner: {self.players[self.ci].name} ({self.ci})")
            print("------------")

        # end-of-round checks
        win = False
        for p in self.players:
            # calculate scores
            self.scores[p.id] += p.hand.size()

            # check for winner
            if p.hand.is_empty():
                p.wins += 1
                win = True

        # end loop if someone wins
        return not win

    def trick_loop(self):
        """
        Stuff that's done in a trick
        """
        # get play from player
        play = self.players[self.ci].play(self.get_data())
        is_valid = Utils.is_valid_play(play, self.get_data())

        if not is_valid:
            print(self.get_data())
            raise ValueError(
                f"Invalid play from {self.players[self.ci].name}: tried {play} on {self.play_to_beat}"
            )

        # remove cards from hand, update hand size
        self.players[self.ci].hand.remove(play)
        self.hand_sizes[self.players[self.ci].id] -= len(play)

        # update round history
        self.round_history[-1].append((self.players[self.ci].id, play))

        if self.verbose:
            print(
                f"{self.players[self.ci].id} played {play if play != [] else '[  ]'} | Remaining: {self.players[self.ci].hand}"
            )

        # stop if player has no cards left
        if self.players[self.ci].hand.is_empty():
            return False

        # player passed
        if play == []:
            self._passes += 1
        else:
            self._passes = 0
            self.play_to_beat = play.copy()

        self.ci = (self.ci + 1) % 4  # next player, loop around
        self.trick_start = False
        self.round_start = False

        # 3 passes = trick ends
        if self._passes == 3:
            self._passes = 0
            return False
        else:
            return True

    def get_data(self) -> dict:
        """
        `hand`: A list of card strings that are the card(s) in your hand.
        `play_to_beat`: The current best play of the trick. If no such play exists (you are the first play in the trick), this will be an empty list.
        `round_history`: A list of *trick_history* entries.
        A *trick_history* entry is a list of *trick_play* entries.
        Each *trick_play* entry is a `(player_no, play)` 2-tuple, where `player_no` is an integer between 0 and 3 (inclusive) indicating which player made the play, and `play` is the play that said player made, which will be a list of card strings.
        `trick_start`: A boolean indicating whether or not the trick has just started.
        `round_start`: A boolean indicating whether or not the round has just started.
        `player_id`: An integer between 0 and 3 (inclusive) indicating which player number you are in the game.
        `hand_sizes`: A 4 size list of integers representing the number of cards each player has in their hand, in player number order.
        `scores`: A 4 size list of integers representing the score of each player at the start of this round, in player number order.
        `round_no`: An integer between 0 and 9 (inclusive) indicating which round number is currently being played.
        """
        return {
            "hand": list(self.players[self.ci].hand),
            "play_to_beat": self.play_to_beat,
            "round_history": self.round_history,
            "trick_start": self.trick_start,  # start of trick or not
            "round_start": self.round_start,  # start of round or not
            "player_id": self.players[self.ci].id,
            "hand_sizes": self.hand_sizes,
            "scores": self.scores,
            "round_no": self.round_no,
        }

    def reset(self):
        self.ci = 0
        self.trick_start = True
        self.round_start = True

        self.play_to_beat = []
        self.hand_sizes = [13, 13, 13, 13]

    def init(self):
        # TODO: find a better name for this and reset()
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

        if self.verbose:
            print("Players:")
            for player in self.players:
                print(f"{player.id}: {player.hand}")
            print(f"Order: {[player.id for player in self.players]}")
            print("------------")

    def start(self):
        # 100 games
        self.game_loop()

        # print results
        print(f"{self.ROUND_LIMIT} rounds results:")
        self.players.sort(key=lambda x: x.name)

        for player in self.players:
            print(f"{player.name} ({player.id}): {player.wins}")

        print("------------")
