from app.main import get_human_age


def test_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_minimum_cat_and_dog_age() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_transition_ages() -> None:
    assert get_human_age(14, 14) == [0, 0]
    assert get_human_age(24, 24) == [2, 2]
    assert get_human_age(28, 28) == [3, 2]


def test_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_partial_transition_cat() -> None:
    assert get_human_age(18, 0) == [2, 0]
    assert get_human_age(32, 0) == [4, 0]


def test_partial_transition_dog() -> None:
    assert get_human_age(0, 18) == [0, 2]
    assert get_human_age(0, 33) == [0, 4]


def test_independent_calculations() -> None:
    assert get_human_age(15, 24) == [1, 2]
    assert get_human_age(24, 15) == [2, 1]
