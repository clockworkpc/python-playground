from base import Base
from typing import List

class CoinChange(Base):
    def __init__(self, value: str):
        self.value = value

    @staticmethod
    def min_coins(coins: List[int], amount: int) -> int:
        """
        Computes the minimum number of coins required to make up the given amount.
        Uses bottom-up dynamic programming.

        :param coins: List of coin denominations.
        :param amount: The target amount to reach.
        :return: Minimum number of coins needed, or -1 if not possible.
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

