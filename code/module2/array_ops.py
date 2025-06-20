from base import Base
from typing import List, Union, Any
from itertools import chain
import re

class ArrayOps(Base):
    def __init__(self, value: int):
        self.value = value    

    @staticmethod
    def double_array(nums: List[int]) -> List[int]:
        """Returns a new list where each integer is multiplied by 2."""
        return [n * 2 for n in nums]

    @staticmethod
    def reverse_array(data: Union[List[int], List[List[int]]]) -> List[int]:
        """Reverses the order of elements in a 1D or 2D list."""
        return data[::-1]

    @staticmethod
    def concat_arrays(a: List[Any], b: List[Any]) -> List[Any]:
        """Concatenates two lists into one."""
        return a + b

