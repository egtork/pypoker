import argparse
import cProfile
import timeit
from . import rank
from .deck import Deck

profile_number = 1
make_hand_repeat = 5
rank_function_repeat = 2
N = 1000
hands = []


def setup_hands():
    global hands
    hands.clear()
    for i in range(N):
        d = Deck()
        hand = []
        for j in range(5):
            hand.append(d.deal())
        hands.append(sorted(hand, reverse=True))


def test_make_hand():
    for hand in hands:
        rank.make_hand(hand)


def test_fn(fn):
    for hand in hands:
        fn(hand)


def benchmark_make_hand():
    setup = (
        "from __main__ import setup_hands, test_make_hand, test_fn; "
        "from __main__ import rank; "
        " setup_hands()"
    )
    timer = timeit.Timer("test_make_hand()", setup=setup)
    t = timer.repeat(repeat=make_hand_repeat, number=profile_number)
    hands_per_second = N / (sum(t) / make_hand_repeat)
    print(f"Hands per second: {int(hands_per_second):,}")


def benchmark_rank_functions():
    setup = (
        "from __main__ import setup_hands, test_make_hand, test_fn; "
        "from __main__ import rank; "
        " setup_hands()"
    )
    functions = (
        "rank.best_straight_flush_hand",
        "rank.best_four_of_a_kind_hand",
        "rank.best_full_house_hand",
        "rank.best_flush_hand",
        "rank.best_straight_hand",
        "rank.best_three_of_a_kind_hand",
        "rank.best_two_pair_hand",
        "rank.best_pair_hand",
        "rank.best_high_card_hand",
    )
    for fn in functions:
        timer = timeit.Timer(f"test_fn({fn})", setup=setup)
        t = timer.repeat(repeat=rank_function_repeat, number=profile_number)
        hands_per_second = N / (sum(t) / rank_function_repeat)
        print(f"{fn: <32}: {int(hands_per_second):,}")


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
        benchmark_rank_functions()
        benchmark_make_hand()
