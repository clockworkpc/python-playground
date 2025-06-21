from typing import List

class Module2:
    @staticmethod
    def repeat_string(a: str, b: int) -> str:
        return a * 3

    @staticmethod
    def is_palindrome(a: str) -> bool:
        return a == a[::-1]

    @staticmethod
    def string_length(a: str) -> int:
        return len(a)

    @staticmethod
    def capitalize_words(words: str) -> str:
        ary = [word.capitalize() for word in words.split()] 
        return ' '.join(ary)

    @staticmethod
    def join_with_dash(chars: List[str]) -> str:
        return '-'.join(chars)

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def is_even(a: int) -> bool:
        return a % 2 == 0

    @staticmethod
    def floor_divide(a: int, b: int) -> int:
        return a // b

    @staticmethod
    def round_to_int(a: float) -> int:
        return round(a)

    @staticmethod
    def abs_value(a: int) -> int:
        return abs(a)

    @staticmethod
    def merge_lists(a: List[int], b: List[int]) -> List[int]:
        return a + b

    @staticmethod
    def list_difference(a: List[int], b: List[int]) -> List[int]:
        return list(set(a) - set(b))

    @staticmethod
    def list_intersection(a: List[int], b: List[int]) -> List[int]:
        return list(set(a) & set(b))

    @staticmethod
    def list_max(a: List[int]) -> int:
        return max(a)

    @staticmethod
    def list_min(a: List[int]) -> int:
        return min(a)

    @staticmethod
    def unique_elements(a: List[int]) -> List[int]:
        return list(set(a))

    @staticmethod
    def filter_even(nums: List[int]) -> List[int]:
        return [num for num in nums if num % 2 == 0]

    @staticmethod
    def count_occurrences(nums: List[int], e: int) -> int:
        return len([num for num in nums if num == e])

    @staticmethod
    def list_to_string(nums: List[int]) -> str:
        return ','.join([str(num) for num in nums])

    @staticmethod
    def list_length(a: List[int]) -> int:
        return len(a)


