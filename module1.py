from typing import List, TypeVar, Callable
from functools import wraps

T = TypeVar("T")
U = TypeVar("U")

def safe_transform(fn: Callable[[List[T]], List[U]]) -> Callable[[List[T]], List[U]]:
    @wraps(fn)
    def wrapper(nums: List[T]) -> List[U]:
        if not nums:
            return []
        try:
            return fn(nums)
        except TypeError:
            return []
    return wrapper


@safe_transform
def increment_by_index(nums: List[int]) -> List[int]:
    return [val + i for i, val in enumerate(nums)]

@safe_transform
def modulo_alternator(nums: List[int]) -> List[int]:
    return [val % 2 for val in nums]

@safe_transform
def running_total(nums: List[int]) -> List[int]:
    total = 0
    result = []
    for val in nums:
        total += val
        result.append(total)
    return result

@safe_transform
def double_negatives(nums: List[int]) -> List[int]:
    return [val * 2 if val < 0 else val for val in nums]

@safe_transform
def absolute_shift(nums: List[int]) -> List[int]:
    new_nums = []
    for i, val in enumerate(nums):
        addend = abs(nums[i-1]) if i > 0 else 0
        new_nums.append(val + addend)
    return new_nums
