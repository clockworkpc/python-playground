
import pytest

# Checking Adjacent Cells in 2D Arrays in Python
def test_adjacent_cells_basic():
    grid = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ]
    assert get_adjacent_cells(grid, 1, 1) == [1, 1, 1, 1]

# Horizontal Move Identification in a Game Board
def test_horizontal_moves():
    board = [
        ["X", ".", "X"],
        ["X", "X", "."]
    ]
    assert horizontal_moves(board, 0) == [(0, 1)]

# Spotting the Landing Area
def test_landing_area_detection():
    area = [
        ["L", ".", "L"],
        [".", ".", "."],
        ["L", ".", "L"]
    ]
    assert find_landing_area(area) == [(1, 1)]

# Assessing Strategic Placement on a Game Board
def test_strategic_placement():
    board = [
        ["S", ".", "S"],
        [".", "T", "."],
        ["S", ".", "S"]
    ]
    assert assess_placement(board) == True

# Magical Chessboard: Discovering the Next Move
def test_next_chess_move():
    chessboard = [
        [".", ".", "."],
        [".", "K", "."],
        [".", ".", "."]
    ]
    assert next_chess_move(chessboard, 1, 1) in [(0, 0), (0, 2), (2, 0), (2, 2)]

# Counting Corner 'E's in Submatrices
def test_count_corner_Es():
    grid = [
        ["E", ".", "E"],
        [".", ".", "."],
        ["E", ".", "E"]
    ]
    assert count_corner_Es(grid, 3, 3) == 4
