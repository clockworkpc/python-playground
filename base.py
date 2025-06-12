from typing import List, Callable, TypeVar
from functools import wraps

T = TypeVar("T")
U = TypeVar("U")

class Base:
    """
    A namespace for our two “safe transform” decorators.
    """

    @staticmethod
    def safe_transform_numeric(fn: Callable[[List[int]], List[int]]) -> Callable[[List[int]], List[int]]:
        """
        Decorator for List[int] -> List[int] functions:
          1. Returns [] if the input list is empty.
          2. Raises TypeError if any element is not an int.
        """
        @wraps(fn)
        def wrapper(nums: List[int]) -> List[int]:
            if not nums:
                return []
            if not all(isinstance(x, int) for x in nums):
                raise TypeError(f"All elements must be int, got {nums!r}")
            return fn(nums)
        return wrapper

    @staticmethod
    def safe_transform_string(fn: Callable[[str], str]) -> Callable[..., str]:
        """
        Decorator for str -> str functions:
          1. Returns "" if the input string is empty or missing.
          2. Otherwise returns fn(s), letting other errors bubble up.
        """
        @wraps(fn)
        def wrapper(s: str = "") -> str:
            if not s:
                return ""
            return fn(s)
        return wrapper

