import pytest
from code.course1.bookshelf import Bookshelf


# Columnar ZigZag and Reverse Traversal of Matrices
def test_columnar_zigzag():
    matrix = [[1, 2], [3, 4]]
    assert Bookshelf.columnar_zigzag(matrix) == [1, 3, 4, 2]


def test_columnar_reverse():
    matrix = [[1, 2], [3, 4]]
    assert Bookshelf.columnar_reverse(matrix) == [4, 3, 2, 1]


# Reverse the Bookshelf Traversal Pattern in Python
def test_reverse_traversal():
    matrix = [["A", "B"], ["C", "D"]]
    assert Bookshelf.reverse_traversal(matrix) == ["C", "D", "A", "B"]


# Add Direction Switch Logic to Bookshelf Traversal
def test_zigzag_traversal():
    matrix = [["A", "B"], ["C", "D"], ["E", "F"]]
    expected = ["A", "B", "D", "C", "E", "F"]
    assert Bookshelf.zigzag_traversal(matrix) == expected


#
# # Vertical Library Traverse Challenge
# def test_vertical_library_traverse():
#     matrix = [["A", "B"], ["C", "D"]]
#     expected = ["A", "C", "B", "D"]
#     assert Bookshelf.vertical_library_traverse(matrix) == expected
#
#
# # Zigzag Bookshelf Traversal Challenge
# def test_zigzag_challenge():
#     matrix = [["A", "B"], ["C", "D"]]
#     expected = ["A", "C", "D", "B"]
#     assert Bookshelf.zigzag_challenge(matrix) == expected
