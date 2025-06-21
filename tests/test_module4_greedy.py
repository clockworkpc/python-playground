import pytest
from code.module4_greedy import Module4

def test_min_coins():
    assert Module4.min_coins([1, 2, 5], 11) == 3

def test_greedy_max_sum():
    assert Module4.greedy_max_sum([1, 2, 3]) == 6

def test_select_tasks():
    assert Module4.select_tasks([[1, 2], [2, 3]]) == [[1, 2], [2, 3]]

def test_interval_scheduling():
    assert Module4.interval_scheduling([1, 2], [2, 3], [3, 4]) == 3

def test_min_number_of_meetings():
    assert Module4.min_number_of_meetings([0, 30], [5, 10], [15, 20]) == 2
