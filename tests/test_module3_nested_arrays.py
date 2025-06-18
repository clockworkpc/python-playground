# type: ignore[arg-type]

from code.module3.arrays import Arrays
import pytest

def test_flatten_2x2():
    assert Arrays.flatten_2d([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_flatten_empty():
    assert Arrays.flatten_2d([]) == []

def test_flatten_single_row():
    assert Arrays.flatten_2d([[5, 6]]) == [5, 6]

def test_flatten_single_column():
    assert Arrays.flatten_2d([[1], [2], [3]]) == [1, 2, 3]

def test_flatten_mixed_sizes():
    assert Arrays.flatten_2d([[1, 2], [3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]

def test_sum_nested_small():
    assert Arrays.sum_nested_matrix([[1, 2], [3]]) == 6

def test_sum_nested_empty_rows():
    assert Arrays.sum_nested_matrix([[], [], [1]]) == 1

def test_sum_nested_all_zero():
    assert Arrays.sum_nested_matrix([[0, 0], [0]]) == 0

def test_sum_nested_mixed():
    assert Arrays.sum_nested_matrix([[1, -1], [2, -2]]) == 0

def test_sum_nested_large():
    assert Arrays.sum_nested_matrix([[10]*10 for _ in range(10)]) == 1000
