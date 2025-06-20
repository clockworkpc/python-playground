from base import Base
from typing import List, Dict
from collections import Counter

class Hashmaps(Base):
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def count_frequencies(items: List[str]) -> Dict[str, int]:
        """Counts how many times each string appears in the input list and returns a frequency dictionary."""
        return dict(Counter(items))

    @staticmethod
    def invert_dict(d: Dict[str, str]) -> Dict[str, str]:
        """Inverts the keys and values of the input dictionary (assumes values are unique)."""
        inverted_dict = {}
        for k, v in d.items():
            inverted_dict[v] = k
        return inverted_dict

