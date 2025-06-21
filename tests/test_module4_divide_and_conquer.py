import pytest
from code.module4_divide_and_conquer import Module4

def test_binary_search():
    assert Module4.binary_search([1, 2, 3, 4, 5], 3) == 2

def test_merge_sort():
    assert Module4.merge_sort([3, 1, 2]) == [1, 2, 3]

def test_max_subarray_sum():
    assert Module4.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_closest_pair():
    assert Module4.closest_pair([0, 0], [3, 4], [7, 7]) == 5

def test_count_inversions():
    assert Module4.count_inversions([2, 4, 1, 3, 5]) == 3
