# type: ignore[arg-type]

from code.module4.subarray import Subarray
import pytest

def test_all_positive():
    assert Subarray.max_subarray_sum([1, 2, 3, 4]) == 10

def test_mixed_numbers():
    assert Subarray.max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4,-1,2,1]

def test_single_element():
    assert Subarray.max_subarray_sum([5]) == 5

def test_all_negative():
    assert Subarray.max_subarray_sum([-3, -1, -2]) == -1

def test_alternating():
    assert Subarray.max_subarray_sum([1, -2, 3, -1, 4]) == 6

