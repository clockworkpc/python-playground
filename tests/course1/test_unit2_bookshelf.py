
import pytest

# Columnar ZigZag and Reverse Traversal of Matrices
def test_columnar_zigzag_and_reverse():
    matrix = [[1, 2], [3, 4]]
    zigzag, reverse = columnar_zigzag_and_reverse(matrix)
    assert zigzag == [1, 3, 4, 2]
    assert reverse == [4, 3, 2, 1]

# Reverse the Bookshelf Traversal Pattern in Python
def test_reverse_bookshelf_traversal():
    shelves = [["A", "B"], ["C", "D"]]
    assert reverse_bookshelf_traversal(shelves) == ["C", "D", "A", "B"]

# Repairing the Library Bookshelf Traversal
def test_repair_bookshelf_traversal():
    shelves = [["X", "Y"], ["Z", "W"]]
    assert repair_bookshelf_traversal(shelves) == ["Z", "W", "X", "Y"]

# Add Direction Switch Logic to Bookshelf Traversal
def test_zigzag_bookshelf_traversal():
    shelves = [["A", "B"], ["C", "D"], ["E", "F"]]
    expected = ["A", "B", "D", "C", "E", "F"]
    assert zigzag_bookshelf_traversal(shelves) == expected

# Vertical Library Traverse Challenge
def test_vertical_library_traverse():
    shelves = [["A", "B"], ["C", "D"]]
    expected = ["A", "C", "B", "D"]
    assert vertical_library_traverse(shelves) == expected

# Zigzag Bookshelf Traversal Challenge
def test_zigzag_bookshelf_challenge():
    shelves = [["A", "B"], ["C", "D"]]
    expected = ["A", "C", "D", "B"]
    assert zigzag_bookshelf_challenge(shelves) == expected
