import pytest
from code.module4.two_pointers import TwoPointers


def test_has_pair_with_sum():
    assert TwoPointers.has_pair_with_sum([1, 2, 4, 4], 8) == True


def test_remove_duplicates():
    assert TwoPointers.remove_duplicates([1, 1, 2]) == [1, 2]


def test_two_sum_indices():
    assert TwoPointers.two_sum_indices([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_indices():
    assert TwoPointers.two_sum_indices([2, 7, 11, 15], 10) == []


def test_move_zeroes():
    assert TwoPointers.move_zeroes([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_reverse_string():
    assert TwoPointers.reverse_string(["h", "e", "l", "l", "o"]) == [
        "o",
        "l",
        "l",
        "e",
        "h",
    ]
