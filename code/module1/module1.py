from base import Base
from typing import List

class Module1(Base):
    @staticmethod
    def concatenate_strings(a: str, b: str) -> str:
        return f"{a} {b}"

    @staticmethod
    def uppercase(a:str) -> str:
        return a.upper()

    @staticmethod
    def strip_whitespace(a: str) -> str:
        return a.strip()

    @staticmethod
    def find_substring(a: str, b: str) -> int:
        return a.find(b)

    @staticmethod
    def replace_substring(a: str, b: str, c: str) -> str:
        return a.replace(b, c)

    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def divide(a: int, b: int) -> float:
        return a / b

    @staticmethod
    def modulus(a: int, b: int) -> int:
        return a % b

    @staticmethod
    def add_floats(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def power(a: int, b: int) -> int:
        return a ** b

    @staticmethod
    def append_to_list(a: list, b: int) -> list:
        a.append(b)
        return a

    @staticmethod
    def extend_list(a: list, b: list) -> list:
        return a + b

    @staticmethod
    def pop_from_list(a: list) -> int:
        return a.pop()

    @staticmethod
    def remove_from_list(a: list, b: int) -> list:
        a.remove(2)
        return a

    @staticmethod
    def sort_list(a: list) -> list:
        a.sort(reverse=False)
        return a
    
    @staticmethod
    def reverse_list(a: list) -> list:
        a.sort(reverse=True)
        return a

    @staticmethod
    def index_of_element(a: List[str], b: str) -> int:
        return a.index(b)

    @staticmethod
    def slice_list(a: List[int], start: int, length: int) -> List[int]:
        return a[start:length]

    @staticmethod
    def double_elements(a: List[int]) -> List[int]:
        return [n * 2 for n in a]

    @staticmethod
    def sum_list(a: List[int]) -> int:
        return sum(a)
