from base import Base
from typing import List

class Arrays(Base):
    def __init__(self, value: int):
        self.value = value    

    @staticmethod
    @Base.safe_transform_numeric
    def array_doubler(nums: List[int]) -> List[int]:
        return [val * 2 for val in nums]

    @staticmethod
    @Base.safe_transform_numeric
    def even_filter(nums: List[int]) -> List[int]:
        return [val for val in nums if val % 2 == 0]

    @staticmethod
    @Base.safe_transform_numeric
    def every_other_element(nums: List[int]) -> List[int]:
        return [val for i, val in enumerate(nums) if i % 2 == 0]

    @staticmethod
    @Base.safe_transform_numeric
    def last_digit_extractor(nums: List[int]) -> List[int]:
        return [abs(num) % 10 for num in nums]

    @staticmethod
    @Base.safe_transform_numeric
    def index_parity_mask(nums: List[int]) -> List[int]:
        return [val * -1 if i % 2 == 0 else val for i, val in enumerate(nums)]
