from base import Base
from typing import List, Union, Any, Optional
from itertools import chain
import re

class Arrays(Base):
    def __init__(self, value: str):
        self.value = value

    _rotation_registry = {}

    @staticmethod
    def sum_nested_matrix(matrix: List[List[int]]) -> int:
        return sum(sum(row) for row in matrix)

    @staticmethod
    def flatten_2d(nested: List[List[int]]) -> List[int]:
        return [item for sublist in nested for item in sublist]
        
    @staticmethod
    def filter_evens(nums: List[int]) -> List[int]:
        return [n for n in nums if n % 2 == 0]

    @staticmethod
    def double_normal(nums: List[int]) -> List[int]:
        return [n * 2 for n in nums if n]

    @staticmethod
    def square_return(nums: List[int]) -> List[int]:
        return [n * n for n in nums if n]

    @staticmethod
    def process_and_filter(nums: List[int]) -> List[int]:
        filtered = Arrays.filter_evens(nums)
        return Arrays.double_normal(filtered)

    @staticmethod
    def filter_and_square_evens(nums: List[int]) -> List[int]:
        filtered = Arrays.filter_evens(nums)
        return Arrays.square_return(filtered)
    
    @staticmethod
    def transpose(matrix: List[List[int]]) -> List[List[int]]:
        return list(map(list, zip(*matrix)))
    
    @staticmethod
    def merge_sorted_arrays(a: List[int], b: List[int]) -> List[int]:
        # Two-pointer method
        i, j = 0, 0  # Pointers for list a and list b
        merged = []

        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1

        # Add remaining elements if any
        merged.extend(a[i:])
        merged.extend(b[j:])

        return merged

