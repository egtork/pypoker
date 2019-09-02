from poker import Card, hand

test_cases = [
    {
        "hand": "7c",
        "cards_unsorted": ("7c",),
        "cards_sorted": ("7c",)},
    {
        "hand": "7cJdTh",
        "cards_unsorted": ("7c", "Jd", "Th"),
        "cards_sorted": ("Jd", "Th", "7c"),
    },
    {
        "hand": "2c5hThJsKd",
        "cards_unsorted": ("2c", "5h", "Th", "Js", "Kd"),
        "cards_sorted": ("Kd", "Js", "Th", "5h", "2c"),
    },
]


def test_hand():
    for tc in test_cases:
        cards_sorted = hand(tc["hand"])
        for i, card in enumerate(cards_sorted):
            assert card == Card(tc["cards_sorted"][i])
        cards_unsorted = hand(tc["hand"], sort=False)
        for i, card in enumerate(cards_unsorted):
            assert card == Card(tc["cards_unsorted"][i])
