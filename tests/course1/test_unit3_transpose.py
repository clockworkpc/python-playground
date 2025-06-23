
import pytest

# Transposing Matrices in Python
def test_transpose_matrix_square():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    expected = [
        [1, 3],
        [2, 4]
    ]
    assert transpose_matrix(matrix) == expected

def test_transpose_matrix_rectangular():
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    expected = [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    assert transpose_matrix(matrix) == expected

# Restaurant Seating Arrangement Transposition
def test_transpose_seating_chart():
    seating = [
        ["A1", "A2"],
        ["B1", "B2"]
    ]
    expected = [
        ["A1", "B1"],
        ["A2", "B2"]
    ]
    assert transpose_seating(seating) == expected

# Transpose the Seating Chart in Reverse Order
def test_transpose_seating_chart_reversed():
    seating = [
        ["R1", "R2"],
        ["S1", "S2"]
    ]
    expected = [
        ["S1", "R1"],
        ["S2", "R2"]
    ]
    assert transpose_seating_reverse(seating) == expected

# Reflecting a Square Matrix Over Secondary Diagonal
def test_reflect_secondary_diagonal():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    expected = [
        [4, 2],
        [3, 1]
    ]
    assert reflect_over_secondary_diagonal(matrix) == expected
