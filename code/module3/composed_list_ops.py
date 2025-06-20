from base import Base
from code.module3.list_ops import ListOps
from typing import List, Union, Any, Optional
from itertools import chain
import re

class ComposedListOps(Base):
    @staticmethod
    def process_and_filter(nums: List[int]) -> List[int]:
        """Filter even numbers and then double each of them."""
        filtered = ListOps.filter_evens(nums)
        return ListOps.double_normal(filtered)

    @staticmethod
    def filter_and_square_evens(nums: List[int]) -> List[int]:
        """Filter even numbers and then square each of them."""
        filtered = ListOps.filter_evens(nums)
        return ListOps.square_return(filtered)
