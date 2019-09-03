from poker import hand
import poker.rank as rank


def test_best_high_card_hand():
    h_in = hand("4d6sQd8cTh")
    h_out = rank.best_high_card_hand(h_in)
    assert h_out == h_in


def test_best_pair_hand():
    tests = [
        (hand("AhAdTh8d6s"), hand("AhAdTh8d6s", sort=False)),
        (hand("AhThTd8d6s"), hand("ThTdAh8d6s", sort=False)),
        (hand("AhTh8d6s6h"), hand("6s6hAhTh8d", sort=False)),
        (hand("AhTh8d8s8h5d4s"), hand("8d8sAhTh8h", sort=False)),
        (hand("3d3sAhThTd8d6s"), hand("ThTdAh8d6s", sort=False)),
        (hand("AhTh8d8s6s5d4d"), hand("8d8sAhTh6s", sort=False)),
        (hand("AhQdTh8d6s"), None),
    ]
    for input, expected_output in tests:
        assert rank.best_pair_hand(input) == expected_output


def test_best_two_pair_hand():
    tests = [
        (hand("TdThAsAc3d"), hand("AsAcTdTh3d", sort=False)),
        (hand("TdThJdJhJs3d2d"), hand("JdJhTdThJs", sort=False)),
        (hand("TdThAsAc3d3hKs"), hand("AsAcTdThKs", sort=False)),
        (hand("AhQdTh8d6s"), None),
    ]
    for input, expected_output in tests:
        assert rank.best_two_pair_hand(input) == expected_output


def test_best_three_of_a_kind_hand():
    tests = [
        (hand("AhAdAs8d6s"), hand("AhAdAs8d6s", sort=False)),
        (hand("AhThTdTs6s"), hand("ThTdTsAh6s", sort=False)),
        (hand("3d3sAhThTdTs6s"), hand("ThTdTsAh6s", sort=False)),
        (hand("AhTh6d6s6h"), hand("6d6s6hAhTh", sort=False)),
        (hand("QcQdQhQsAc"), hand("QcQdQhAcQs", sort=False)),
        (hand("AhTh8d8s8h5d4d"), hand("8d8s8hAhTh", sort=False)),
        (hand("AhQdTh8d6s"), None),
    ]
    for input, expected_output in tests:
        assert rank.best_three_of_a_kind_hand(input) == expected_output


def test_best_straight_hand():
    tests = [
        (hand("JdAhKhQdTd"), hand("AhKhQdJdTd", sort=False)),
        (hand("5hAh4d3d2s"), hand("5h4d3d2sAh", sort=False)),
        (hand("Ts9s7h6h5d4d3d"), hand("7h6h5d4d3d", sort=False)),
        (hand("Ts9s8h6h5d4d3d"), None),
    ]
    for input, expected_output in tests:
        assert rank.best_straight_hand(input) == expected_output


def test_best_flush_hand():
    tests = [
        (hand("3h4h6h7h8h"), hand("8h7h6h4h3h", sort=False)),
        (hand("2sAs5s6s9s"), hand("As9s6s5s2s", sort=False)),
        (hand("2sAs4d5s4h6s9s"), hand("As9s6s5s2s", sort=False)),
    ]
    for input, expected_output in tests:
        assert rank.best_flush_hand(input) == expected_output


def test_best_full_house_hand():
    tests = [
        (hand("3dAd3sAs3h"), hand("3d3s3hAdAs", sort=False)),
        (hand("Ad3sAs3hAh"), hand("AdAsAh3s3h", sort=False)),
        (hand("Kd3sKs3hKh3d2d"), hand("KdKsKh3s3h", sort=False)),
        (hand("2d2hAd3sAs3hAh"), hand("AdAsAh3s3h", sort=False)),
        (hand("2d2h3d3h4d4hAh"), None),
    ]
    for input, expected_output in tests:
        assert rank.best_full_house_hand(input) == expected_output


def test_best_four_of_a_kind_hand():
    tests = [
        (hand("9d5h5s5c5d"), hand("5h5s5c5d9d", sort=False)),
        (hand("QhTsTdThTcAd3h"), hand("TsTdThTcAd", sort=False)),
        (hand("QhQdQsTsTdThAd"), None),
    ]
    for input, expected_output in tests:
        assert rank.best_four_of_a_kind_hand(input) == expected_output


def test_best_straight_flush_hand():
    tests = [
        (hand("ThJhQhKhAh"), hand("AhKhQhJhTh", sort=False)),
        (hand("Ah5h4h3h2h"), hand("5h4h3h2hAh", sort=False)),
        (hand("AhKhJhTh9h8h7h"), hand("JhTh9h8h7h", sort=False)),
        (hand("AhKhJhTh9h8h7d"), None),
        (hand("TdJhQhKhAh"), None),
    ]
    for input, expected_output in tests:
        sf_hand, flush_hand = rank.best_straight_flush_hand(input)
        assert sf_hand == expected_output


def test_make_hand():
    hand_tests = (
        (
            hand("ThJhQhKhAh"),
            hand("AhKhQhJhTh", sort=False),
            rank.HandRank.STRAIGHT_FLUSH,
        ),
        (
            hand("9d5h5s5c5d"),
            hand("5h5s5c5d9d", sort=False),
            rank.HandRank.FOUR_OF_A_KIND,
        ),
        (
            hand("Ad3sAs3hAh3d2d"),
            hand("AdAsAh3s3h", sort=False),
            rank.HandRank.FULL_HOUSE,
        ),
        (
            hand("2sAs5s6s9sAdAc"),
            hand("As9s6s5s2s", sort=False),
            rank.HandRank.FLUSH,
        ),
        (
            hand("Ts9s7h6h5d4d3d"),
            hand("7h6h5d4d3d", sort=False),
            rank.HandRank.STRAIGHT,
        ),
        (
            hand("AhTh8d8s8h5d4d"),
            hand("8d8s8hAhTh", sort=False),
            rank.HandRank.THREE_OF_A_KIND,
        ),
        (
            hand("TdThAsAc3d3hKs"),
            hand("AsAcTdThKs", sort=False),
            rank.HandRank.TWO_PAIR,
        ),
        (
            hand("3dQsAhThTd8d6s"),
            hand("ThTdAhQs8d", sort=False),
            rank.HandRank.PAIR,
        ),
        (
            hand("3d5s6s9dJhQsAc"),
            hand("AcQsJh9d6s", sort=False),
            rank.HandRank.HIGH_CARD,
        ),
    )
    for input, expected_hand, expected_rank in hand_tests:
        hand_out, rank_out = rank.make_hand(input)
        assert hand_out == expected_hand
        assert rank_out == expected_rank
