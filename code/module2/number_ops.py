from base import Base
from typing import List
from itertools import chain
import re

class NumberOps(Base):
    def __init__(self, value: int):
        self.value = value    

    @staticmethod
    @Base.safe_transform_binary_numeric
    def add_numbers(a: int, b: int) -> int:
        return a + b

    @staticmethod
    @Base.safe_transform_unary_list
    def split_digits(a: int) -> List[int]:
        return [int(digit) for digit in str(a)]
