from base import Base
from typing import List, Union, Any, Optional
from itertools import chain
import re

class ArrayMerging(Base):
    @staticmethod
    def merge_sorted_arrays(a: List[int], b: List[int]) -> List[int]:
        """Merge two sorted arrays."""
        i, j = 0, 0
        merged = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                merged.append(a[i])
                i += 1
            else:
                merged.append(b[j])
                j += 1
        merged.extend(a[i:])
        merged.extend(b[j:])
        return merged

    @staticmethod
    def interleave_arrays(a: List[int], b: List[int]) -> List[int]:
        """Interleave two arrays element by element."""
        zipped_pairs = list(zip(a, b))
        merged = [item for pair in zipped_pairs for item in pair]
        merged.extend(a[len(b):])
        merged.extend(b[len(a):])
        return merged
