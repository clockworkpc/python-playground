from base import Base
from typing import List, Union, Any, Optional

class Subarray(Base):
    def __init__(self, value: List[int]):
        self.value = value

    @staticmethod
    def max_crossing_sum(arr: List[int], left: int, mid: int, right: int) -> int:
        # Include elements on left of mid
        left_sum = float('-inf')
        total = 0
        for i in range(mid, left - 1, -1):
            total += arr[i]
            left_sum = max(left_sum, total)

        # Include elements on right of mid
        right_sum = float('-inf')
        total = 0
        for i in range(mid + 1, right + 1):
            total += arr[i]
            right_sum = max(right_sum, total)

        return left_sum + right_sum

    @staticmethod
    def max_subarray_divide_conquer(arr: List[int], left: int, right: int) -> int:
        # Base case: one element
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        return max(
            Subarray.max_subarray_divide_conquer(arr, left, mid),           # Left half
            Subarray.max_subarray_divide_conquer(arr, mid + 1, right),      # Right half
            Subarray.max_crossing_sum(arr, left, mid, right)                # Cross middle
        )

    @staticmethod
    def max_subarray_sum(arr: List[int]) -> int:
        if not arr:
            return 0
        return Subarray.max_subarray_divide_conquer(arr, 0, len(arr) - 1)
