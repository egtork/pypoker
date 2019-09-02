from random import shuffle as shuffle_fn
from .card import Card

SUITS = "shdc"
RANKS = "AKQJT98765432"


class Deck:
    def __init__(self, shuffle: bool = True):
        self.i = 0
        self.cards = []
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(r + s))
        if shuffle:
            self.shuffle()

    def shuffle(self):
        shuffle_fn(self.cards)
        self.i = 0

    def deal(self):
        if len(self) == 0:
            raise IndexError("No more cards in deck.")
        card = self.cards[self.i]
        self.i += 1
        return card

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration()
        return self.deal()

    def __len__(self):
        return len(self.cards) - self.i
