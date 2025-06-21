from base import Base
from typing import List, Union, Any, Optional
from itertools import chain
import re

class MatrixOps(Base):
    def __init__(self, value: str):
        self.value = value

    _rotation_registry = {}

    @staticmethod
    @Base.enforce_types
    def sum_nested_matrix(matrix: List[List[int]]) -> int:
        return sum(sum(row) for row in matrix)

    @staticmethod
    def flatten_2d(matrix: List[List[int]]) -> List[int]:
        ary = []
        for row in matrix:
            for cell in row:
                ary.append(cell)
        return ary
    
    @staticmethod
    def flatten_2d(matrix: List[List[int]]) -> List[int]:
        return [cell for row in matrix for cell in row]

    @staticmethod
    def transpose(matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))


