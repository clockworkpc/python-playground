from base import Base
from typing import List, Union, Any, Optional


class SubarrayOps(Base):
    def __init__(self, value: List[int]):
        # Store the input list as an instance variable
        self.value = value

    @staticmethod
    def has_pair_with_sum(nums: List[int], target: int) -> bool:
        # Initialize an empty set to store previously seen numbers
        seen = set()

        # Iterate through each number in the input list
        for num in nums:
            # Check if the complement (target - num) is already in the set
            if (target - num) in seen:
                # If found, return True since a pair exists that sums to target
                return True

            # Otherwise, add the current number to the set
            seen.add(num)

        # If no such pair was found after the loop, return False
        return False
