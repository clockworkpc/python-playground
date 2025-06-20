# type: ignore[arg-type]

from code.module4.max_subarray import MaxSubarray
import pytest


def test_all_positive():
    ms = MaxSubarray([1, 2, 3, 4])
    assert ms.max_subarray_sum() == 10

def test_mixed_numbers():
    ms = MaxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert ms.max_subarray_sum() == 6  # [4,-1,2,1]

def test_single_element():
    ms = MaxSubarray([5])
    assert ms.max_subarray_sum() == 5

def test_all_negative():
    ms = MaxSubarray([-3, -1, -2])
    assert ms.max_subarray_sum() == -1

def test_alternating():
    ms = MaxSubarray([1, -2, 3, -1, 4])
    assert ms.max_subarray_sum() == 6

