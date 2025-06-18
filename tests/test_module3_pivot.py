# type: ignore[arg-type]

from code.module3.arrays import Arrays
import pytest

def test_transpose_2x2():
    assert Arrays.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transpose_3x2():
    assert Arrays.transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

def test_transpose_single_row():
    assert Arrays.transpose([[1, 2, 3]]) == [[1], [2], [3]]

def test_transpose_single_column():
    assert Arrays.transpose([[1], [2], [3]]) == [[1, 2, 3]]

def test_transpose_square_matrix():
    assert Arrays.transpose([[0, 1], [2, 3]]) == [[0, 2], [1, 3]]
