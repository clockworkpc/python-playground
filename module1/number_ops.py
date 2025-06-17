from base import Base
from typing import List

class NumberOps(Base):
    def __init__(self, value: int):
        self.value = value    

    @staticmethod
    @Base.safe_transform_numeric
    def increment_by_index(nums: List[int]) -> List[int]:
        return [val + i for i, val in enumerate(nums)]

    @staticmethod
    @Base.safe_transform_numeric
    def modulo_alternator(nums: List[int]) -> List[int]:
        return [val % 2 for val in nums]

    @staticmethod
    @Base.safe_transform_numeric
    def running_total(nums: List[int]) -> List[int]:
        total = 0
        result = []
        for val in nums:
            total += val
            result.append(total)
        return result

    @staticmethod
    @Base.safe_transform_numeric
    def double_negatives(nums: List[int]) -> List[int]:
        return [val * 2 if val < 0 else val for val in nums]

    @staticmethod
    @Base.safe_transform_numeric
    def absolute_shift(nums: List[int]) -> List[int]:
        new_nums = []
        for i, val in enumerate(nums):
            addend = abs(nums[i-1]) if i > 0 else 0
            new_nums.append(val + addend)
        return new_nums
