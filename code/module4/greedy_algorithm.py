from base import Base
from typing import List, Union, Any, Optional

class GreedyAlgorithm(Base):
    def __init__(self, value: str):
        self.value = value

    # @staticmethod
    # def collect_coins(
    #     collected_coins: List[int] = None, coins: List[int] = None, amount: int = 0
    # ) -> List[int]:
    #     if collected_coins == None:
    #         collected_coins = []
    #
    #     if amount == 0:
    #         return collected_coins
    #
    #     max_coin = max((x for x in coins if x <= amount), default=None)
    #
    #     if max_coin is None:
    #         return collected_coins
    #     else:
    #         collected_coins.append(max_coin)
    #         amount -= max_coin
    #
    #     print(collected_coins)
    #     return GreedyAlgorithm.max_coin(collected_coins, coins, amount)

    @staticmethod
    def min_coins(coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1
