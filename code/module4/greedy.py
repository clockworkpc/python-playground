from typing import List, Dict, Any


class Greedy:
    def min_coins(coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

    def greedy_max_sum(nums: List[int]) -> int:
        return sum([num for num in nums if num > 0])

    def select_tasks(arr: List[List[int]]) -> List[List[int]]:
        selected = []

        if not arr:
            return selected

        sorted_pairs = sorted(arr, key=lambda x: (x[1], x[0]))
        selected.append(sorted_pairs[0])

        for pair in sorted_pairs[1:]:
            if pair[0] >= selected[-1][1]:
                selected.append(pair)

        return selected

    def non_overlapping_pairs_count(*pairs: List[int]) -> int:
        # pairs is a tuple of lists, not a list of lists
        return len(Greedy.select_tasks(list(pairs)))
