from enum import Enum, IntEnum


class Rank(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __repr__(self):
        if self.value < 10:
            return str(self.value)
        else:
            return self.name[0]

    def __str__(self):
        if self.value < 10:
            return str(self.value)
        else:
            return self.name[0]


str_to_rank = {
    "2": Rank.TWO,
    "3": Rank.THREE,
    "4": Rank.FOUR,
    "5": Rank.FIVE,
    "6": Rank.SIX,
    "7": Rank.SEVEN,
    "8": Rank.EIGHT,
    "9": Rank.NINE,
    "T": Rank.TEN,
    "J": Rank.JACK,
    "Q": Rank.QUEEN,
    "K": Rank.KING,
    "A": Rank.ACE,
}


class Suit(Enum):
    CLUBS = "c"
    DIAMONDS = "d"
    HEARTS = "h"
    SPADES = "s"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.value


str_to_suit = {
    "c": Suit.CLUBS,
    "d": Suit.DIAMONDS,
    "h": Suit.HEARTS,
    "s": Suit.SPADES,
}


class Card:
    def __init__(self, s: str):
        assert len(s) == 2
        assert s[1] in (Suit.CLUBS.value, Suit.DIAMONDS.value,
                        Suit.HEARTS.value, Suit.SPADES.value)
        self.rank = str_to_rank[s[0]]
        self.suit = str_to_suit[s[1]]

    def __eq__(self, other):
        return self.rank == other.rank

    def __ne__(self, other):
        return self.rank != other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __gte__(self, other):
        return self.rank >= other.rank

    def __lte__(self, other):
        return self.rank <= other.rank

    def __repr__(self):
        return str(self.rank) + str(self.suit)
