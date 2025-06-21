from typing import List, Dict, Any
import math
from itertools import count


class Subtask:
    def sum_range(a: int, b: int) -> int:
        return sum(list(range(a, b + 1)))

    def fibonacci(a: int) -> int:
        if a < 0:
            raise ValueError("Input should be a non-negative integer.")
        elif a == 0:
            return 0
        elif a == 1:
            return 1

        # Initialize the first two Fibonacci numbers
        ary = [0, 1]

        # Generate Fibonacci numbers up to the a-th index
        for x in range(2, a + 1):  # Start from 2 to a
            next_fib = ary[x - 1] + ary[x - 2]  # Sum of the last two numbers
            ary.append(next_fib)

        return ary[a]

    def factorial(n: int) -> int:
        return math.prod(list(range(1, n + 1)))

    def greatest_common_divisor(a: int, b: int) -> int:
        if a == b:
            return a

        smaller_num = a if a < b else b
        ary = []
        for x in list(range(1, smaller_num + 1)):
            common_divisor = a % x == 0 and b % x == 0
            if common_divisor:
                ary.append(x)

        return max(ary)

    def least_common_multiple(a: int, b: int) -> int:
        smaller = a if a < b else b
        for i in count(start=smaller, step=smaller):
            match = i % b == 0
            print(f"{i} % {b} == 0 ? {match}")
            if match:
                return i
