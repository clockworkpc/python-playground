from base import Base
from typing import List, Union, Any, Optional
from itertools import chain
import re

class ListOps(Base):
    @staticmethod
    def filter_evens(nums: List[int]) -> List[int]:
        """Keep only even numbers."""
        return [n for n in nums if n % 2 == 0]

    @staticmethod
    def double_normal(nums: List[int]) -> List[int]:
        """Double all non-zero values."""
        return [n * 2 for n in nums if n]

    @staticmethod
    def square_return(nums: List[int]) -> List[int]:
        """Square all non-zero values."""
        return [n * n for n in nums if n]
