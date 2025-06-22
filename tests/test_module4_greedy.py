import pytest
from code.module4.greedy import Greedy


def test_min_coins():
    assert Greedy.min_coins([1, 2, 5], 11) == 3


def test_greedy_max_sum():
    # All positive numbers
    assert Greedy.greedy_max_sum([1, 2, 3]) == 6

    # Includes zero
    assert Greedy.greedy_max_sum([0, 1, 2]) == 3

    # Includes negative numbers
    assert Greedy.greedy_max_sum([-1, 2, 3]) == 5
    assert Greedy.greedy_max_sum([-5, -2, 4]) == 4
    assert Greedy.greedy_max_sum([-1, -2, -3]) == 0

    # Mixed with zero and negatives
    assert Greedy.greedy_max_sum([-1, 0, 5]) == 5
    assert Greedy.greedy_max_sum([0, 0, 0]) == 0

    # Single element cases
    assert Greedy.greedy_max_sum([10]) == 10
    assert Greedy.greedy_max_sum([-10]) == 0
    assert Greedy.greedy_max_sum([0]) == 0

    # Empty input
    assert Greedy.greedy_max_sum([]) == 0

    # Large input
    assert Greedy.greedy_max_sum([1] * 1000) == 1000
    assert Greedy.greedy_max_sum([-1] * 1000) == 0


def test_select_tasks():
    # Original case: back-to-back intervals
    assert Greedy.select_tasks([[1, 2], [2, 3]]) == [[1, 2], [2, 3]]

    # Overlapping tasks: should pick one with earlier end
    assert Greedy.select_tasks([[1, 3], [2, 5], [4, 6]]) == [[1, 3], [4, 6]]

    # Fully nested tasks: should pick the shortest
    assert Greedy.select_tasks([[1, 10], [2, 3], [4, 5]]) == [[2, 3], [4, 5]]

    # Unordered input
    assert Greedy.select_tasks([[5, 6], [1, 2], [3, 4]]) == [[1, 2], [3, 4], [5, 6]]

    # All overlapping: only one can be chosen
    assert Greedy.select_tasks([[1, 4], [2, 5], [3, 6]]) == [[1, 4]]

    # No tasks
    assert Greedy.select_tasks([]) == []

    # Single task
    assert Greedy.select_tasks([[1, 2]]) == [[1, 2]]

    # Multiple with same end time
    assert Greedy.select_tasks([[1, 3], [2, 3], [0, 3]]) == [[0, 3]]

    # Long chain of compatible intervals
    assert Greedy.select_tasks([[0, 1], [1, 2], [2, 3], [3, 4]]) == [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 4],
    ]

    # Task with zero length
    assert Greedy.select_tasks([[1, 1], [1, 2], [2, 3]]) == [[1, 1], [1, 2], [2, 3]]


def test_interval_scheduling():
    assert Greedy.non_overlapping_pairs_count([1, 2], [2, 3], [3, 4]) == 3


def test_min_number_of_meetings():
    assert Greedy.non_overlapping_pairs_count([0, 30], [5, 10], [15, 20]) == 2
