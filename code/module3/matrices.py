from base import Base
from typing import List, Union, Any, Optional
from itertools import chain
import re

_rotation_registry = {}

def register_rotation(name):
    def decorator(fn):
        _rotation_registry[name] = fn
        return fn
    return decorator

class Matrices(Base):
    def __init__(self, value: str):
            self.value = value

    @staticmethod
    @register_rotation("rotate_90_clockwise")
    def rotate_90_clockwise(matrix: List[List[int]]) -> List[List[int]]:
        return [list(reversed(col)) for col in zip(*matrix)]

    @staticmethod
    @register_rotation("rotate_90_anticlockwise")
    def rotate_90_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
        return [list(col) for col in zip(*reversed(matrix))]

    @staticmethod
    @register_rotation("rotate_180_clockwise")
    def rotate_180_clockwise(matrix: List[List[int]]) -> List[List[int]]:
        return [row[::-1] for row in matrix[::-1]]

    @staticmethod
    @register_rotation("rotate_180_anticlockwise")
    def rotate_180_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
        return Arrays.rotate_180_clockwise(matrix)

    @staticmethod
    @register_rotation("rotate_270_clockwise")
    def rotate_270_clockwise(matrix: List[List[int]]) -> List[List[int]]:
        return Arrays.rotate_90_anticlockwise(matrix)

    @staticmethod
    @register_rotation("rotate_270_anticlockwise")
    def rotate_270_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
        return Arrays.rotate_90_clockwise(matrix)

    @staticmethod
    def rotate_matrix(degrees: int, clockwise: bool, matrix: List[List[int]]) -> List[List[Optional[int]]]:
        if not matrix or not any(matrix):
            raise Exception("Matrix must be provided")

        max_len = max(len(row) for row in matrix)
        padded = [row + [None] * (max_len - len(row)) for row in matrix]

        if degrees not in [90, 180, 270]:
            raise Exception(f"Degrees must be one of 90, 180, 270")

        method_name = f"rotate_{degrees}_{'clockwise' if clockwise else 'anticlockwise'}"
        rotation_fn = _rotation_registry.get(method_name)
        
        if not rotation_fn:
            raise Exception(f"No registered rotation method for {method_name}")

        return rotation_fn(padded)

