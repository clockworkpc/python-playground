import pytest
from code.course1.adjacent import Adjacent


# Checking Adjacent Cells in 2D Arrays in Python
def test_adjacent_cells_basic():
    grid = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    assert Adjacent.get_adjacent_cells(grid, 1, 1) == [1, 1, 1, 1]


# Horizontal Move Identification in a Game Board
def test_horizontal_moves():
    board = [["X", ".", "X"], ["X", "X", "."]]
    assert Adjacent.horizontal_moves(board, 0) == [(0, 1)]


# Spotting the Landing Area
def test_landing_area_detection():
    area = [["L", ".", "L"], [".", ".", "."], ["L", ".", "L"]]
    assert Adjacent.find_landing_area(area) == [(1, 1)]


# No landing area at all
def test_landing_area_none():
    area = [["L", "L", "L"], ["L", ".", "L"], ["L", "L", "L"]]
    assert Adjacent.find_landing_area(area) == []


# Multiple landing areas in different rows
def test_multiple_landing_areas():
    area = [[".", ".", "."], ["L", ".", "L"], [".", ".", "."]]
    assert Adjacent.find_landing_area(area) == [(0, 1), (2, 1)]


# Single row with one landing spot
def test_single_row_landing():
    area = [[".", ".", ".", ".", "."]]
    assert Adjacent.find_landing_area(area) == [(0, 1), (0, 2), (0, 3)]


# Edge columns should be excluded
def test_no_landing_on_edges():
    area = [[".", ".", "."]]
    assert Adjacent.find_landing_area(area) == [(0, 1)]


# Landing surrounded by land
def test_landing_surrounded_by_land():
    area = [["L", ".", ".", ".", "L"]]
    assert Adjacent.find_landing_area(area) == [(0, 2)]


# Empty board
def test_empty_board():
    area = []
    assert Adjacent.find_landing_area(area) == []


# Non-rectangular board (should be handled or fail gracefully)
def test_jagged_board():
    area = [[".", ".", "."], [".", "."], [".", ".", "."]]
    try:
        result = Adjacent.find_landing_area(area)
        assert result == [(0, 1), (2, 1)]
    except IndexError:
        # Acceptable if the method isn't designed for ragged arrays
        pass


# # Assessing Strategic Placement on a Game Board
# def test_strategic_placement():
#     board = [["S", ".", "S"], [".", "T", "."], ["S", ".", "S"]]
#     assert Adjacent.assess_placement(board) == True
#
#
# # Magical Chessboard: Discovering the Next Move
# def test_next_chess_move():
#     chessboard = [[".", ".", "."], [".", "K", "."], [".", ".", "."]]
#     assert Adjacent.next_chess_move(chessboard, 1, 1) in [
#         (0, 0),
#         (0, 2),
#         (2, 0),
#         (2, 2),
#     ]
#
#
# # Counting Corner 'E's in Submatrices
# def test_count_corner_Es():
#     grid = [["E", ".", "E"], [".", ".", "."], ["E", ".", "E"]]
#     assert Adjacent.count_corner_Es(grid, 3, 3) == 4
