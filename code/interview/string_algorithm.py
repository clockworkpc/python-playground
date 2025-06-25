from typing import List


class StringAlgorithm:
    def string_permutation(s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)
