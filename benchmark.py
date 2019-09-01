from rank import make_hand
from deck import Deck
import cProfile

N = 20000
hands = []


def setup_hands():
    global hands
    hands.clear()
    for i in range(N):
        d = Deck()
        hand = []
        for j in range(5):
            hand.append(d.deal())
        hands.append(hand)


def test_make_hand():
    for hand in hands:
        make_hand(hand)


if __name__ == "__main__":
    # import timeit
    setup_hands()
    cProfile.run('test_make_hand()')
    # setup = "from __main__ import setup_hands, test_make_hand; setup_hands()"
    # timer = timeit.Timer("test_make_hand()", setup=setup)
    # print(timer.repeat(repeat=3, number=10))
