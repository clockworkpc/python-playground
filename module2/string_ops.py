from base import Base
from typing import List
from itertools import chain
import re

class StringOps(Base):
    def __init__(self, value: int):
        self.value = value    

    @staticmethod
    @Base.safe_transform_multiple_strings
    def split_words(*args: str) -> List[str]:
        if len(args) == 1:
            return args[0].split()
        else:
            clean = lambda x: re.sub(r'[^A-Za-z0-9]', '', x)
            cleaned = [clean(s) for s in args if s]
            return list(chain.from_iterable(cleaned))


