from base import Base
from typing import List, Union, Any, Optional

class Subpair(Base):
    def __init__(self, value: List[int]):
        self.value = value

    @staticmethod
    def has_pair_with_sum(nums: List[int], target: int) -> bool:
        dp = [float('inf')] * (target + 1)
        dp[0]

