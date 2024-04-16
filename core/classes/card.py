class Card:
    def __init__(self, rank: str, suit: str):
        if (rank.upper() not in Card.rank_order()) or (
            suit.upper() not in Card.suit_order()
        ):
            raise ValueError("Invalid card: " + rank + suit)

        self.rank = rank  # 3-9, 0 (10), J, Q, K, A, 2
        self.suit = suit  # H, D, C, S

    def is_high(self):
        return self.rank in ["J", "Q", "K", "A", "2"]

    def is_low(self):
        return not self.is_high()

    def __str__(self):
        return self.rank + self.suit

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other):
        # rank first
        if Card.rank_order().index(self.rank) < Card.rank_order().index(other.rank):
            return True

        # suit second
        elif Card.rank_order().index(self.rank) == Card.rank_order().index(other.rank):
            return Card.suit_order().index(self.suit) < Card.suit_order().index(
                other.suit
            )

        else:
            return False

    @classmethod
    def lowest(cls):
        return cls(cls.rank_order()[0], cls.suit_order()[0])

    @classmethod
    def from_str(cls, card_str: str):
        card_str = card_str.upper()
        return cls(card_str[0], card_str[1])

    # rank order
    @classmethod
    def rank_order(cls):
        return ["3", "4", "5", "6", "7", "8", "9", "0", "J", "Q", "K", "A", "2"]

    @classmethod
    def suit_order(cls):
        return ["D", "C", "H", "S"]
