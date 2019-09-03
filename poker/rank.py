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


def get_flush_cards(cards):
    suits = {
        Suit.HEARTS: [],
        Suit.SPADES: [],
        Suit.DIAMONDS: [],
        Suit.CLUBS: [],
    }
    for card in cards:
        suits[card.suit].append(card)
    for suit in suits.keys():
        if len(suits[suit]) >= 5:
            return suits[suit]
    return None


def best_straight_flush_hand(cards: List[Card]):
    flush_cards = get_flush_cards(cards)
    if flush_cards:
        straight_flush_hand = best_straight_hand(flush_cards)
        return straight_flush_hand, flush_cards[:5]
    return None, None


def best_four_of_a_kind_hand(cards: List[Card]):
    ranks = defaultdict(list)
    for card in cards:
        ranks[card.rank].append(card)
        if len(ranks[card.rank]) == 4:
            for kicker in cards:
                if kicker.rank != card.rank:
                    return ranks[card.rank] + [kicker]
    return None


def best_full_house_hand(cards: List[Card]):
    trips_cards = None
    for i in range(len(cards) - 2):
        if cards[i].rank == cards[i + 1].rank == cards[i + 2].rank:
            trips_cards = [cards[i], cards[i + 1], cards[i + 2]]
            kickers = cards[:i] + cards[i + 3 :]
            break
    if not trips_cards:
        return None
    for i in range(len(kickers) - 1):
        if kickers[i].rank == kickers[i + 1].rank:
            return trips_cards + [kickers[i], kickers[i + 1]]
    return None


def best_flush_hand(cards: List[Card]):
    flush_cards = get_flush_cards(cards)
    if flush_cards:
        return flush_cards[:5]
    return None


def best_straight_hand(cards: List[Card]):
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
    for i in range(len(cards) - 2):
        if cards[i].rank == cards[i + 1].rank == cards[i + 2].rank:
            trips_cards = [cards[i], cards[i + 1], cards[i + 2]]
            kickers = cards[:i] + cards[i + 3 :]
            return trips_cards + kickers[:2]
    return None


def best_two_pair_hand(cards: List[Card]):
    first_pair = None
    i = 0
    while i < len(cards) - 1:
        if cards[i].rank == cards[i + 1].rank:
            if first_pair:
                hand = first_pair + [cards[i], cards[i + 1]]
                for kicker in cards:
                    if kicker not in hand:
                        return hand + [kicker]
            else:
                first_pair = [cards[i], cards[i + 1]]
            i += 1
        i += 1
    return None


def best_pair_hand(cards: List[Card]):
    for i in range(len(cards) - 1):
        if cards[i].rank == cards[i + 1].rank:
            pair_cards = [cards[i], cards[i + 1]]
            kickers = cards[:i] + cards[i + 2 :]
            return pair_cards + kickers[:3]
    return None


def best_high_card_hand(cards: List[Card]):
    return cards[:5]


def make_hand(cards: List[Card]):
    assert 5 <= len(cards) <= 7
    cards = sorted(cards, reverse=True)
    hand, flush_hand = best_straight_flush_hand(cards)
    if hand:
        return hand, HandRank.STRAIGHT_FLUSH
    hand = best_four_of_a_kind_hand(cards)
    if hand:
        return hand, HandRank.FOUR_OF_A_KIND
    hand = best_full_house_hand(cards)
    if hand:
        return hand, HandRank.FULL_HOUSE
    if flush_hand:
        return flush_hand, HandRank.FLUSH
    hand = best_straight_hand(cards)
    if hand:
        return hand, HandRank.STRAIGHT
    hand = best_three_of_a_kind_hand(cards)
    if hand:
        return hand, HandRank.THREE_OF_A_KIND
    hand = best_two_pair_hand(cards)
    if hand:
        return hand, HandRank.TWO_PAIR
    hand = best_pair_hand(cards)
    if hand:
        return hand, HandRank.PAIR
    hand = best_high_card_hand(cards)
    return hand, HandRank.HIGH_CARD
