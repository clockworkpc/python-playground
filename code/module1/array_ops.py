from base import Base
from typing import List

class ArrayOps(Base):
    def __init__(self, value: int):
        self.value = value    

    @staticmethod
    @Base.safe_transform_numeric
    def array_doubler(nums: List[int]) -> List[int]:
        """Return a new list where each element is doubled from the input list."""
        return [val * 2 for val in nums]

    @staticmethod
    @Base.safe_transform_numeric
    def even_filter(nums: List[int]) -> List[int]:
        """Return a list containing only even numbers from the input list."""
        return [val for val in nums if val % 2 == 0]

    @staticmethod
    @Base.safe_transform_numeric
    def every_other_element(nums: List[int]) -> List[int]:
        """Return every other element from the input list, starting with index 0."""
        return [val for i, val in enumerate(nums) if i % 2 == 0]

    @staticmethod
    @Base.safe_transform_numeric
    def last_digit_extractor(nums: List[int]) -> List[int]:
        """Extract and return the last digit of each number in the input list."""
        return [abs(num) % 10 for num in nums]

    @staticmethod
    @Base.safe_transform_numeric
    def index_parity_mask(nums: List[int]) -> List[int]:
        """Negate elements at even indices, leave odd-indexed elements unchanged."""
        return [val * -1 if i % 2 == 0 else val for i, val in enumerate(nums)]

