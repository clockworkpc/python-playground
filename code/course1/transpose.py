from typing import List, Union, Any


class Transpose:
    def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        for col in range(cols):
            new_row = []
            for row in range(rows):
                new_row.append(matrix[row][col])
            result.append(new_row)

        return result

    def reverse_transpose(matrix: List[List[Any]]) -> List[List[Any]]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        for col in range(cols):
            new_row = []
            for row in reversed(range(rows)):
                new_row.append(matrix[row][col])
            result.append(new_row)

        return result

    def reflect_over_secondary_diagonal(matrix: List[List[Any]]) -> List[List[Any]]:
        if not matrix or not matrix[0]:
            return []

        rows = len(matrix)
        cols = len(matrix[0])
        result = []

        for col in reversed(range(cols)):
            new_row = []
            for row in reversed(range(rows)):
                new_row.append(matrix[row][col])
            result.append(new_row)

        return result
