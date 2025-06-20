# type: ignore[arg-type]

from code.module3.rotate_matrix import RotateMatrix
import pytest

def test_rotate_2x2():
    assert RotateMatrix.call(90, True, [[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

def test_rotate_2x2_extra():
    assert RotateMatrix.call(90, True, [[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

def test_rotate_3x3():
    assert RotateMatrix.call(90, True, [[1,2,3], [4,5,6], [7,8,9]]) == [[7,4,1], [8,5,2], [9,6,3]]

def test_rotate_identity():
    assert RotateMatrix.call(90, True, [[1,0], [0,1]]) == [[0,1], [1,0]]

def test_rotate_all_same():
    assert RotateMatrix.call(90, True, [[5,5],[5,5]]) == [[5,5],[5,5]]

def test_rotate_large_fixed():
    assert RotateMatrix.call(90, True, [[0,1,0],[0,1,0],[0,1,0]]) == [[0,0,0],[1,1,1],[0,0,0]]
