from typing import List
from .card import Card


def hand(s: str, sort: bool = True) -> List[Card]:
    num_cards = len(s) // 2
    cards = []
    for i in range(num_cards):
        cards.append(Card(s[2*i:2*i + 2]))
    if sort:
        return sorted(cards, reverse=True)
    return cards
