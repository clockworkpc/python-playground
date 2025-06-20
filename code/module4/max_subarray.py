from base import Base
from typing import List

class MaxSubarray(Base):
    def __init__(self, arr: List[int]):
        """Initialize with the input list of integers."""
        self.arr = arr

    def max_crossing_sum(self, left: int, mid: int, right: int) -> int:
        """
        Finds the maximum subarray sum that crosses the midpoint.
        """
        left_sum = float('-inf')
        total = 0
        for i in range(mid, left - 1, -1):
            total += self.arr[i]
            left_sum = max(left_sum, total)

        right_sum = float('-inf')
        total = 0
        for i in range(mid + 1, right + 1):
            total += self.arr[i]
            right_sum = max(right_sum, total)

        return left_sum + right_sum

    def max_subarray_divide_conquer(self, left: int, right: int) -> int:
        """
        Recursively computes the maximum subarray sum using divide and conquer.
        """
        if left == right:
            return self.arr[left]

        mid = (left + right) // 2

        return max(
            self.max_subarray_divide_conquer(left, mid),
            self.max_subarray_divide_conquer(mid + 1, right),
            self.max_crossing_sum(left, mid, right)
        )

    def max_subarray_sum(self) -> int:
        """
        Computes the maximum subarray sum for the entire list.
        """
        if not self.arr:
            return 0
        return self.max_subarray_divide_conquer(0, len(self.arr) - 1)

