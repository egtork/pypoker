from enum import IntEnum


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


rank_to_str = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J',
               'Q', 'K', 'A']

str_to_rank = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}


class Card:
    def __init__(self, s: str):
        assert len(s) == 2
        assert s[1] in ('c', 'd', 'h', 's')
        self.rank = str_to_rank[s[0]]
        self.suit = s[1]

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
        return rank_to_str[self.rank] + self.suit
