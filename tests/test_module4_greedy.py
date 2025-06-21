import pytest
from code.module4.greedy import Greedy


def test_min_coins():
    assert Greedy.min_coins([1, 2, 5], 11) == 3


def test_greedy_max_sum():
    assert Greedy.greedy_max_sum([1, 2, 3]) == 6


# def test_select_tasks():
#     assert Greedy.select_tasks([[1, 2], [2, 3]]) == [[1, 2], [2, 3]]
#
# def test_interval_scheduling():
#     assert Greedy.interval_scheduling([1, 2], [2, 3], [3, 4]) == 3
#
# def test_min_number_of_meetings():
#     assert Greedy.min_number_of_meetings([0, 30], [5, 10], [15, 20]) == 2
