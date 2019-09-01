from card import Card
from random import shuffle as shuffle_fn

suits = "shdc"
ranks = "AKQJT98765432"


class Deck:
    def __init__(self, shuffle: bool = True):
        self.i = 0
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(r + s))
        if shuffle:
            self.shuffle()

    def shuffle(self):
        self.i = 0
        shuffle_fn(self.cards)

    def deal(self):
        card = self.cards[self.i]
        self.i += 1
        return card

    # def __len__(self):
    #     return len(self.cards) - self.i

    # def __iter__(self):
    #     for i in range(len(self.cards)):
    #         yield self.cards[i]

    # # def __next__(self):
    # #     for i in range(len(self.cards)):
    # #         yield self.deal()
