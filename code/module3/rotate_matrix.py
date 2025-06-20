from base import Base
from typing import List, Union, Any, Optional
from itertools import chain
import re

# Internal registry to map rotation methods by name
_rotation_registry = {}

# Decorator to register rotation methods in the internal registry
def register_rotation(name):
    def decorator(fn):
        _rotation_registry[name] = fn
        return fn
    return decorator

class RotateMatrix(Base):
    def __init__(self, value: str):
        self.value = value

    # Rotate 90° clockwise: transpose and then reverse each row
    @staticmethod
    @register_rotation("rotate_90_clockwise")
    def rotate_90_clockwise(matrix: List[List[int]]) -> List[List[int]]:
        return [list(reversed(col)) for col in zip(*matrix)]

    # Rotate 90° anticlockwise: reverse rows, then transpose
    @staticmethod
    @register_rotation("rotate_90_anticlockwise")
    def rotate_90_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
        return [list(col) for col in zip(*reversed(matrix))]

    # Rotate 180° clockwise (same as 180° anticlockwise): reverse both rows and columns
    @staticmethod
    @register_rotation("rotate_180_clockwise")
    def rotate_180_clockwise(matrix: List[List[int]]) -> List[List[int]]:
        return [row[::-1] for row in matrix[::-1]]

    # Rotate 180° anticlockwise reuses the clockwise method
    @staticmethod
    @register_rotation("rotate_180_anticlockwise")
    def rotate_180_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
        return Matrices.rotate_180_clockwise(matrix)  # Fixed: was incorrectly referencing Arrays

    # Rotate 270° clockwise is same as 90° anticlockwise
    @staticmethod
    @register_rotation("rotate_270_clockwise")
    def rotate_270_clockwise(matrix: List[List[int]]) -> List[List[int]]:
        return Matrices.rotate_90_anticlockwise(matrix)  # Fixed: was incorrectly referencing Arrays

    # Rotate 270° anticlockwise is same as 90° clockwise
    @staticmethod
    @register_rotation("rotate_270_anticlockwise")
    def rotate_270_anticlockwise(matrix: List[List[int]]) -> List[List[int]]:
        return Matrices.rotate_90_clockwise(matrix)  # Fixed: was incorrectly referencing Arrays

    # General-purpose rotation dispatcher
    @staticmethod
    def call(degrees: int, clockwise: bool, matrix: List[List[int]]) -> List[List[Optional[int]]]:
        """
        Rotates a matrix by 90, 180, or 270 degrees in the specified direction.
        Pads rows with None values to ensure rectangular shape before rotating.

        :param degrees: The degree of rotation (must be 90, 180, or 270)
        :param clockwise: Direction of rotation; True for clockwise, False for anticlockwise
        :param matrix: A 2D list representing the matrix
        :return: The rotated matrix
        """
        if not matrix or not any(matrix):
            raise Exception("Matrix must be provided")

        # Normalize row lengths by padding with None
        max_len = max(len(row) for row in matrix)
        padded = [row + [None] * (max_len - len(row)) for row in matrix]

        if degrees not in [90, 180, 270]:
            raise Exception("Degrees must be one of 90, 180, 270")

        method_name = f"rotate_{degrees}_{'clockwise' if clockwise else 'anticlockwise'}"
        rotation_fn = _rotation_registry.get(method_name)

        if not rotation_fn:
            raise Exception(f"No registered rotation method for {method_name}")

        return rotation_fn(padded)


