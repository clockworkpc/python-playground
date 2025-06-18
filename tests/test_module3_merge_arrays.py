# type: ignore[arg-type]

from code.module3.arrays import Arrays
import pytest

def test_merge_disjoint():
    assert Arrays.merge_sorted_arrays([1, 3], [2, 4]) == [1, 2, 3, 4]

def test_merge_with_duplicates():
    assert Arrays.merge_sorted_arrays([1, 2, 2], [2, 3]) == [1, 2, 2, 2, 3]

def test_merge_first_empty():
    assert Arrays.merge_sorted_arrays([], [1, 2]) == [1, 2]

def test_merge_second_empty():
    assert Arrays.merge_sorted_arrays([3, 4], []) == [3, 4]

def test_merge_both_empty():
    assert Arrays.merge_sorted_arrays([], []) == []
