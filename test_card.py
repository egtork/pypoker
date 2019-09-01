from card import Card, Rank
import suit as Suit


def test_card():
    test_cases = [
        ('2h', (Rank.TWO, Suit.HEARTS)),
        ('Tc', (Rank.TEN, Suit.CLUBS)),
        ('Js', (Rank.JACK, Suit.SPADES)),
        ('Ad', (Rank.ACE, Suit.DIAMONDS)),
    ]
    for input, (expected_rank, expected_suit) in test_cases:
        c = Card(input)
        assert c.rank == expected_rank
        assert c.suit == expected_suit


def test_card_to_str():
    assert str(Card('2h')) == '2h'
    assert str(Card('Tc')) == 'Tc'
    assert str(Card('Js')) == 'Js'
    assert str(Card('Ad')) == 'Ad'


def test_comparison():
    assert Card('Tc') < Card('Jc')
    assert Card('9h') > Card('4d')
    assert Card('Qd') == Card('Qh')
