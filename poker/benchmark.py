import argparse
import cProfile
import timeit
from .rank import make_hand
from .deck import Deck

profile_number = 1
profile_repeat = 5
N = 10000
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
    parser = argparse.ArgumentParser(description="Poker hand evaluator.")
    parser.add_argument("--profile")
    args = parser.parse_args()
    if args.profile:
        print("Profiling...")
        setup_hands()
        cProfile.run("test_make_hand()")
    else:
        print("Benchmarking...")
        setup = (
            "from __main__ import setup_hands, test_make_hand; setup_hands()"
        )
        timer = timeit.Timer("test_make_hand()", setup=setup)
        t = timer.repeat(repeat=profile_repeat, number=profile_number)
        hands_per_second = N / (sum(t) / profile_repeat)
        print(f"Hands per second: {int(hands_per_second):,}")
