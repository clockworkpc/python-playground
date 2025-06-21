from typing import List, Dict, Any


class TwoPointers:
    def has_pair_with_sum(nums: List[int], b: int) -> bool:
        seen = set()

        for num in nums:
            if num == 0 and b == 0:
                return True

            if b % num == 0:
                target = b // num
                if target in seen:
                    return True

            seen.add(num)

        return False

    def remove_duplicates(nums: List[int]) -> List[int]:
        return list(set(nums))

    def two_sum_indices(nums: List[int], value: int) -> List[int]:
        seen = {}

        def get_key(a: int) -> int:
            return next((k for k, v in seen.items() if v == a), None)

        for i, num in enumerate(nums):
            remainder = value - num
            if remainder in seen:
                return [seen[remainder], i]
            else:
                seen[num] = i

        return []

    def move_zeroes(nums: List[int]) -> List[int]:
        ary = [i for i in nums if i != 0]

        for num in nums:
            if num == 0:
                ary.append(num)
        return ary

    def reverse_string(a: List[str]) -> List[str]:
        return list(reversed(a))
