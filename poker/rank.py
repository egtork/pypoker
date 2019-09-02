from collections import defaultdict
from enum import Enum, auto
from typing import List
from .card import Card, Rank, Suit


class HandRank(Enum):
    HIGH_CARD = auto()
    PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    STRAIGHT = auto()
    FLUSH = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    STRAIGHT_FLUSH = auto()


def is_sorted(cards):
    for i in range(len(cards) - 1):
        if cards[i + 1] > cards[i]:
            return False
    return True


def best_straight_flush_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    suits = defaultdict(list)
    flush_suit = None
    for card in cards:
        suits[card.suit].append(card)
        if len(suits[card.suit]) == 5:
            flush_suit = card.suit
    if flush_suit:
        return best_straight_hand(suits[flush_suit])
    return None


def best_four_of_a_kind_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    ranks = defaultdict(list)
    for card in cards:
        ranks[card.rank].append(card)
        if len(ranks[card.rank]) == 4:
            for kicker in cards:
                if kicker.rank != card.rank:
                    return ranks[card.rank] + [kicker]
    return None


def best_full_house_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    trips_cards = None
    for i in range(len(cards) - 2):
        if cards[i] == cards[i + 1] == cards[i + 2]:
            trips_cards = [cards[i], cards[i + 1], cards[i + 2]]
            kickers = cards[:i] + cards[i + 3 :]
            break
    if not trips_cards:
        return None
    for i in range(len(kickers) - 1):
        if kickers[i] == kickers[i + 1]:
            return trips_cards + [kickers[i], kickers[i + 1]]
    return None


def best_flush_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    suits = {
        Suit.HEARTS: [],
        Suit.SPADES: [],
        Suit.DIAMONDS: [],
        Suit.CLUBS: [],
    }
    for card in cards:
        suits[card.suit].append(card)
        if len(suits[card.suit]) == 5:
            return suits[card.suit]
    return None


def best_straight_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    i = 0
    while i < len(cards) - 3:
        run = [cards[i]]
        while i < len(cards) - 1:
            if cards[i].rank == cards[i + 1].rank:
                i += 1
            elif cards[i].rank == cards[i + 1].rank + 1:
                i += 1
                run.append(cards[i])
                if len(run) == 5:
                    return run
            else:
                i += 1
                break
    if (
        cards[0].rank == Rank.ACE
        and run[0].rank == Rank.FIVE
        and run[-1].rank == Rank.TWO
    ):
        return run + [cards[0]]
    return None


def best_three_of_a_kind_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    for i in range(len(cards) - 2):
        if cards[i] == cards[i + 1] == cards[i + 2]:
            trips_cards = [cards[i], cards[i + 1], cards[i + 2]]
            kickers = cards[:i] + cards[i + 3 :]
            return trips_cards + kickers[:2]
    return None


def best_two_pair_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    ranks = defaultdict(list)
    first_pair = None
    for card in cards:
        ranks[card.rank].append(card)
        if len(ranks[card.rank]) == 2:
            if first_pair:
                for kicker in cards:
                    if (
                        kicker.rank != first_pair[0].rank
                        and kicker.rank != card.rank
                    ):
                        return first_pair + ranks[card.rank] + [kicker]
            else:
                first_pair = ranks[card.rank]
    return None


def best_pair_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            pair_cards = [cards[i], cards[i + 1]]
            kickers = cards[:i] + cards[i + 2 :]
            return pair_cards + kickers[:3]
    return None


def best_high_card_hand(cards: List[Card]):
    assert is_sorted(cards), "Cards not sorted."
    return cards[:5]


hand_functions = (
    (best_straight_flush_hand, HandRank.STRAIGHT_FLUSH),
    (best_four_of_a_kind_hand, HandRank.FOUR_OF_A_KIND),
    (best_full_house_hand, HandRank.FULL_HOUSE),
    (best_flush_hand, HandRank.FLUSH),
    (best_straight_hand, HandRank.STRAIGHT),
    (best_three_of_a_kind_hand, HandRank.THREE_OF_A_KIND),
    (best_two_pair_hand, HandRank.TWO_PAIR),
    (best_pair_hand, HandRank.PAIR),
    (best_high_card_hand, HandRank.HIGH_CARD),
)


def make_hand(cards):
    assert 5 <= len(cards) <= 7
    cards = sorted(cards, reverse=True)
    for hand_fn, hand_rank in hand_functions:
        hand = hand_fn(cards)
        if hand:
            return hand, hand_rank
