# type: ignore[arg-type]

from code.module3.arrays import Arrays
from code.module3.matrices import Matrices
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

def test_rotate_2x2():
    assert Matrices.rotate_90_clockwise([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

def test_rotate_2x2_extra():
    assert Matrices.rotate_matrix(90, True, [[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

def test_rotate_3x3():
    assert Matrices.rotate_matrix(90, True, [[1,2,3], [4,5,6], [7,8,9]]) == [[7,4,1], [8,5,2], [9,6,3]]

def test_rotate_identity():
    assert Matrices.rotate_90_clockwise([[1,0], [0,1]]) == [[0,1], [1,0]]

def test_rotate_all_same():
    assert Matrices.rotate_90_clockwise([[5,5],[5,5]]) == [[5,5],[5,5]]

def test_rotate_large_fixed():
    assert Matrices.rotate_90_clockwise([[0,1,0],[0,1,0],[0,1,0]]) == [[0,0,0],[1,1,1],[0,0,0]]
