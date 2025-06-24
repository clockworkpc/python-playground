from typing import List, Tuple


class Adjacent:
    def get_adjacent_cells(grid: List[List[int]], row: int, col: int) -> List[int]:
        if not grid:
            return []

        rows = len(grid)
        cols = len(grid[0])
        result = []

        if row in range(1, rows):
            north_row = row - 1
            result.append(grid[north_row][col])

        if row in range(0, rows - 1):
            south_row = row + 1
            result.append(grid[south_row][col])

        if col in range(1, cols - 1):
            west_col = col - 1
            result.append(grid[row][west_col])

        if col in range(0, cols):
            east_col = col + 1
            result.append(grid[row][east_col])

        return result

    def horizontal_moves(board: List[List[int]], row_index: int) -> List[Tuple[int]]:
        if not board:
            return []

        result = []

        for index, cell in enumerate(board[row_index]):
            if cell == ".":
                coordinates = (row_index, index)
                result.append(coordinates)

        return result

    def find_landing_area(area: List[List[int]]) -> List[Tuple[int]]:
        if not area:
            return []

        cols = len(area[0])
        result = []

        for row_index, row in enumerate(area):
            for col_index, cell in enumerate(row):
                if col_index in range(1, cols - 1):
                    if cell == ".":
                        if area[row_index][col_index - 1] == ".":
                            if area[row_index][col_index + 1] == ".":
                                coordinates = (row_index, col_index)
                                result.append(coordinates)
        return result
