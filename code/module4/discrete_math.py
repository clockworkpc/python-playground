from typing import List, Dict, Any
import math


class DiscreteMath:
    def is_prime(a: int) -> bool:
        if a in [0, 1]:
            return True

        for x in range(2, a):
            if a % x == 0:
                return False

        return True

    def prime_factors(a: int) -> List[int]:
        if a < 2:
            return []

        factors = []
        current_divisor = 2
        remainder = a

        while remainder > 1:
            if remainder % current_divisor == 0:
                factors.append(current_divisor)
                remainder //= current_divisor
            else:
                current_divisor += 1
                if current_divisor * current_divisor > remainder:
                    factors.append(remainder)
                    break

        return factors

    def modular_exponentiation(a: int, b: int, c: int) -> int:
        return (a**b) % c

    def n_choose_k(n: int, k: int) -> int:
        n_factorial = math.prod(list(range(1, n + 1)))
        k_factorial = math.prod(list(range(1, k + 1)))
        nk_factorial = math.prod(list(range(1, n - k + 1)))
        return n_factorial // (k_factorial * nk_factorial)

    def combinatorics(n: int, k: int) -> int:
        return DiscreteMath.n_choose_k(n, k)

    def count_divisors(a: int) -> int:
        return len([x for x in range(1, a + 1) if a % x == 0])
