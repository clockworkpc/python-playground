
import pytest

# Navigating Adjacent Cells in a Grid: An Exercise in 2D Traversal
def test_adjacent_navigation():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert get_neighbors(grid, 1, 1) == [2, 4, 6, 8]

# Enhance Hiking Trail Path Finder with Diagonal Movements
def test_diagonal_neighbors():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert get_diagonal_neighbors(grid, 1, 1) == [1, 3, 7, 9]

# Mountain Peak Exploration Code Correction
def test_peak_detection():
    elevation = [
        [1, 3, 1],
        [3, 5, 3],
        [1, 3, 1]
    ]
    assert is_peak(elevation, 1, 1) == True

# Add a Function to Navigate to the Next Higher Peak
def test_next_higher_peak():
    elevation = [
        [1, 2],
        [3, 4]
    ]
    assert next_higher_peak(elevation, 0, 0) == (0, 1)

# Add Selection Logic for the Next Hiking Position Based on Elevation
def test_hiking_next_step():
    elevation = [
        [1, 2, 3],
        [2, 1, 4],
        [3, 2, 1]
    ]
    assert next_hiking_position(elevation, 1, 1) == (1, 2)

# Ascending the Mountain - Grid Traversal Challenge
def test_mountain_ascent_path():
    elevation = [
        [1, 2, 3],
        [2, 4, 6],
        [3, 5, 9]
    ]
    assert mountain_ascent_path(elevation, (0, 0)) == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
