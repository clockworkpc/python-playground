# type: ignore[arg-type]

from code.module3.matrix_ops import MatrixOps
import pytest

def test_flatten_2x2():
    assert MatrixOps.flatten_2d([[1, 2], [3, 4]]) == [1, 2, 3, 4]

def test_flatten_empty():
    assert MatrixOps.flatten_2d([]) == []

def test_flatten_single_row():
    assert MatrixOps.flatten_2d([[5, 6]]) == [5, 6]

def test_flatten_single_column():
    assert MatrixOps.flatten_2d([[1], [2], [3]]) == [1, 2, 3]

def test_flatten_mixed_sizes():
    assert MatrixOps.flatten_2d([[1, 2], [3], [4, 5, 6]]) == [1, 2, 3, 4, 5, 6]

def test_sum_nested_small():
    assert MatrixOps.sum_nested_matrix([[1, 2], [3]]) == 6

def test_sum_nested_empty_rows():
    assert MatrixOps.sum_nested_matrix([[], [], [1]]) == 1

def test_sum_nested_all_zero():
    assert MatrixOps.sum_nested_matrix([[0, 0], [0]]) == 0

def test_sum_nested_mixed():
    assert MatrixOps.sum_nested_matrix([[1, -1], [2, -2]]) == 0

def test_sum_nested_large():
    assert MatrixOps.sum_nested_matrix([[10]*10 for _ in range(10)]) == 1000

def test_transpose_2x2():
    assert MatrixOps.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_3x2():
    assert MatrixOps.transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

def test_transpose_single_row():
    assert MatrixOps.transpose([[1, 2, 3]]) == [[1], [2], [3]]

def test_transpose_single_column():
    assert MatrixOps.transpose([[1], [2], [3]]) == [[1, 2, 3]]

def test_transpose_square_matrix():
    assert MatrixOps.transpose([[0, 1], [2, 3]]) == [[0, 2], [1, 3]]

