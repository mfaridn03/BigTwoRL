RANK_ORDER = ["3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A", "2"]
SUIT_ORDER = ["D", "C", "H", "S"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank  # 2-9, T (10), J, Q, K, A
        self.suit = suit  # H, D, C, S

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        # rank first
        if RANK_ORDER.index(self.rank) < RANK_ORDER.index(other.rank):
            return True

        # suit second
        elif RANK_ORDER.index(self.rank) == RANK_ORDER.index(other.rank):
            return SUIT_ORDER.index(self.suit) < SUIT_ORDER.index(other.suit)

        else:
            return False
