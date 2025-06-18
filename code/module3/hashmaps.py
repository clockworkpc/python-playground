from base import Base
from typing import List, Dict
from collections import Counter

class Hashmaps(Base):
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def count_frequencies(items: List[str]) -> Dict[str, int]:
        return dict(Counter(items))
