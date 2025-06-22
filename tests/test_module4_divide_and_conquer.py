import pytest
from code.module4.divide_and_conquer import DivideAndConquer


def test_binary_search():
    # Standard case
    assert DivideAndConquer.binary_search([1, 2, 3, 4, 5], 3) == 2

    # First element
    assert DivideAndConquer.binary_search([1, 2, 3, 4, 5], 1) == 0

    # Last element
    assert DivideAndConquer.binary_search([1, 2, 3, 4, 5], 5) == 4

    # Not in list
    assert DivideAndConquer.binary_search([1, 2, 3, 4, 5], 6) == -1
    assert DivideAndConquer.binary_search([1, 2, 3, 4, 5], 0) == -1

    # Empty list
    assert DivideAndConquer.binary_search([], 3) == -1

    # Single element - present
    assert DivideAndConquer.binary_search([7], 7) == 0

    # Single element - absent
    assert DivideAndConquer.binary_search([7], 3) == -1

    # Two elements
    assert DivideAndConquer.binary_search([4, 8], 8) == 1
    assert DivideAndConquer.binary_search([4, 8], 5) == -1

    # Repeated elements - return any valid index (usually middle one)
    result = DivideAndConquer.binary_search([1, 2, 2, 2, 3], 2)
    assert result in [1, 2, 3]  # acceptable results for duplicates


def test_merge_sort():
    # Already sorted
    assert DivideAndConquer.merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Reverse order
    assert DivideAndConquer.merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Unordered with duplicates
    assert DivideAndConquer.merge_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

    # All same values
    assert DivideAndConquer.merge_sort([2, 2, 2]) == [2, 2, 2]

    # Single element
    assert DivideAndConquer.merge_sort([9]) == [9]

    # Empty list
    assert DivideAndConquer.merge_sort([]) == []

    # Negative numbers
    assert DivideAndConquer.merge_sort([-1, -3, 0, 2]) == [-3, -1, 0, 2]

    # Mix of positive and negative
    assert DivideAndConquer.merge_sort([0, -1, 3, -2, 5]) == [-2, -1, 0, 3, 5]

    # Large input
    assert DivideAndConquer.merge_sort(list(range(100, 0, -1))) == list(range(1, 101))


def test_max_subarray_sum_original_case():
    assert DivideAndConquer.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_max_subarray_sum_all_positive():
    assert DivideAndConquer.max_subarray_sum([1, 2, 3, 4]) == 10


def test_max_subarray_sum_all_negative():
    assert DivideAndConquer.max_subarray_sum([-8, -3, -6, -2, -5]) == -2


def test_max_subarray_sum_single_positive():
    assert DivideAndConquer.max_subarray_sum([7]) == 7


def test_max_subarray_sum_single_negative():
    assert DivideAndConquer.max_subarray_sum([-7]) == -7


def test_max_subarray_sum_two_elements_pos_neg():
    assert DivideAndConquer.max_subarray_sum([2, -1]) == 2


def test_max_subarray_sum_two_elements_neg_pos():
    assert DivideAndConquer.max_subarray_sum([-1, 2]) == 2


def test_max_subarray_sum_max_at_end():
    assert DivideAndConquer.max_subarray_sum([-1, -2, -3, 4]) == 4


def test_max_subarray_sum_max_at_beginning():
    assert DivideAndConquer.max_subarray_sum([4, -1, -2, -3]) == 4


def test_max_subarray_sum_empty_raises():
    with pytest.raises(ValueError):
        DivideAndConquer.max_subarray_sum([])


def test_max_subarray_sum_zeros_and_positives():
    assert DivideAndConquer.max_subarray_sum([0, 0, 0, 1, 0]) == 1


def test_max_subarray_sum_alternating_pos_neg():
    assert DivideAndConquer.max_subarray_sum([-1, 2, -1, 2, -1]) == 3


# def test_closest_pair():
#     assert DivideAndConquer.closest_pair([0, 0], [3, 4], [7, 7]) == 5
#
# def test_count_inversions():
#     assert DivideAndConquer.count_inversions([2, 4, 1, 3, 5]) == 3
