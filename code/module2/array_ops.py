from base import Base
from typing import List, Union, Any
from itertools import chain
import re

class ArrayOps(Base):
    def __init__(self, value: int):
        self.value = value    

    @staticmethod
    def double_array(nums: List[int]) -> List[int]:
        return [n * 2 for n in nums]

    @staticmethod
    def reverse_array(data: Union[List[int], List[List[int]]]) -> List[int]:
        return data[::-1]

    @staticmethod
    def concat_arrays(a: List[Any], b: List[Any]) -> List[Any]:
        return a + b



