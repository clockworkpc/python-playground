from typing import List, Dict, Any


class DivideAndConquer:
    def binary_search(a: List[int], b: int) -> int:
        if b not in a:
            return -1
        return a.index(b)

    def merge_sort(a: List[int]) -> List[int]:
        return list(sorted(a))

    def max_subarray_sum(arr: List[int]) -> int:
        print("start")
        print(f"arr = {arr}")
        if not arr:
            raise ValueError("Input list is empty")

        max_sum = curr_sum = arr[0]

        for i in range(1, len(arr)):
            curr_sum = max(arr[i], curr_sum + arr[i])
            print(f"curr_sum = {curr_sum}")
            max_sum = max(max_sum, curr_sum)
            print(f"max_sum = {max_sum}")

        print("done")
        return max_sum
