from typing import List, Callable, TypeVar, get_origin, get_args
from functools import wraps
from inspect import signature

T = TypeVar("T")
U = TypeVar("U")

class Base:
    @staticmethod
    def enforce_types(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            sig = signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            for name, value in bound.arguments.items():
                expected = func.__annotations__.get(name)
                if expected is None:
                    continue

                try:
                    Base._check_type(value, expected, param=name)
                except TypeError as e:
                    raise TypeError(f"In argument '{name}': {e}")

            return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def _check_type(value, expected, param=None):
        origin = get_origin(expected)
        args = get_args(expected)

        if origin is not None:
            if not isinstance(value, origin):
                raise TypeError(f"expected {origin.__name__}, got {type(value).__name__}")
            if origin is list and args:
                for i, item in enumerate(value):
                    try:
                        Base._check_type(item, args[0])
                    except TypeError as e:
                        raise TypeError(f"{param}[{i}] -> {e}")
        else:
            if not isinstance(value, expected):
                raise TypeError(f"expected {expected.__name__}, got {type(value).__name__}")

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

    @staticmethod
    def safe_transform_binary_numeric(fn: Callable[[int, int], int]) -> Callable[[int, int], int]:
        """
        Decorator for (int, int) -> int methods:
          1. Raises TypeError if either argument is not an int.
        """
        @wraps(fn)
        def wrapper(a: int, b: int) -> int:
            if not isinstance(a, int) or not isinstance(b, int):
                raise TypeError(f"Expected two integers, got {a!r}, {b!r}")
            return fn(a, b)
        return wrapper

    @staticmethod
    def safe_transform_unary_list(fn: Callable[[int], List]) -> Callable[[int], List]:
        """
        Decorator for (int) -> list methods:
          1. Raises TypeError if the argument is not an int.
        """
        @wraps(fn)
        def wrapper(n: int) -> List:
            if not isinstance(n, int):
                raise TypeError(f"Expected an integer, got {n!r}")
            return fn(n)
        return wrapper

    @staticmethod
    def safe_transform_single_string(fn: Callable[[str], List[str]]) -> Callable[[str], List[str]]:
        """
        Decorator for str -> List[str] functions:
          1. Returns [] if the input string is empty.
          2. Otherwise returns a list processed by fn(s).
          3. Raises TypeError if the input is not a string.
        """
        @wraps(fn)
        def wrapper(s: str) -> List[str]:
            if not isinstance(s, str):
                raise TypeError(f"Expected a string, got {s!r}")
            if not s:
                return []
            return fn(s)
        return wrapper

    @staticmethod
    def safe_transform_multiple_strings(fn: Callable[[str], List[str]]) -> Callable[..., List[str]]:
        """
        Decorator for multiple strings -> List[str] functions:
          1. Returns [] if any input string is empty or if no inputs are provided.
          2. Otherwise returns a list processed by fn(*args).
          3. Raises TypeError if any input is not a string.
        """
        @wraps(fn)
        def wrapper(*args: str) -> List[str]:
            if not all(isinstance(arg, str) for arg in args):
                raise TypeError(f"All arguments must be strings, got {args!r}")
            if not args or any(not arg for arg in args):
                return []
            return fn(*args)
        return wrapper
