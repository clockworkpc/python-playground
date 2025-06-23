from typing import List, Tuple


class Bookshelf:
    def setup(matrix: List[List[int]]) -> Tuple[int, int, List[int]]:
        if not matrix or not matrix[0]:
            return [-1, -1, []]
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        return (rows, cols, result)

    def add_book(matrix: List[List[int]], result: List[int], row: int, col: int):
        result.append(matrix[row][col])

    def columnar_zigzag(matrix: List[List[int]]) -> List[int]:
        rows, cols, result = Bookshelf.setup(matrix)
        if rows == -1 or cols == -1:
            return []

        for col in range(cols):
            if col % 2 == 0:
                for row in range(rows):
                    Bookshelf.add_book(matrix, result, row, col)
                    # result.append(matrix[row][col])
            else:
                for row in reversed(range(rows)):
                    Bookshelf.add_book(matrix, result, row, col)
                    # result.append(matrix[row][col])

        return result

    def columnar_reverse(matrix: List[List[int]]) -> List[int]:
        rows, cols, result = Bookshelf.setup(matrix)
        if rows == -1 or cols == -1:
            return []

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                result.append(matrix[row][col])

        return result

    def reverse_traversal(matrix: List[List[int]]) -> List[int]:
        rows, cols, result = Bookshelf.setup(matrix)
        if rows == -1 or cols == -1:
            return []

        for row in reversed(range(rows)):
            for col in range(cols):
                result.append(matrix[row][col])

        return result

    def zigzag_traversal(matrix: List[List[int]]) -> List[int]:
        rows, cols, result = Bookshelf.setup(matrix)
        if rows == -1 or cols == -1:
            return []

        for row in range(rows):
            if row % 2 == 0:
                for col in range(cols):
                    result.append(matrix[row][col])
            else:
                for col in reversed(range(cols)):
                    result.append(matrix[row][col])

        return result
