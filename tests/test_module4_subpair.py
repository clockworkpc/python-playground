# type: ignore[arg-type]

from code.module4.divide_and_conquer_max_subarray import DivideAndConquerMaxSubarray as DC
import pytest

def test_pair_exists():
    assert DC.has_pair_with_sum([1, 2, 4, 7], 6) is True

def test_pair_not_found():
    assert DC.has_pair_with_sum([1, 2, 3], 7) is False

def test_empty_list():
    assert DC.has_pair_with_sum([], 3) is False

def test_single_element():
    assert DC.has_pair_with_sum([5], 10) is False

def test_negative_numbers():
    assert DC.has_pair_with_sum([-3, 1, 4, 6], 3) is True  # -3 + 6

