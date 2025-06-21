import pytest
from code.module3.matrix_ops import MatrixOps


def test_flatten_2x2():
    assert MatrixOps.flatten_2d([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_flatten_2x3():
    assert MatrixOps.flatten_2d([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]


def test_flatten_3x3():
    assert MatrixOps.flatten_2d([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == list(range(1, 10))


def test_transpose_matrix_2x2():
    assert MatrixOps.transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_transpose_matrix_2x4():
    assert MatrixOps.transpose([[1, 2], [3, 4], [5, 6], [7, 8]]) == [
        [1, 3, 5, 7],
        [2, 4, 6, 8],
    ]


def test_transpose_matrix_4x2():
    assert MatrixOps.transpose([[1, 2, 3, 4], [5, 6, 7, 8]]) == [
        [1, 5],
        [2, 6],
        [3, 7],
        [4, 8],
    ]
