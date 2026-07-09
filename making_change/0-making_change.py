#!/usr/bin/python3
"""
Main module for the makeChange function.
"""


def makeChange(coins: list[int], total: int) -> int:
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list[int]): A list of the values of the coins in possession.
        total (int): The target amount to reach.

    Returns:
        int: Fewest number of coins needed, 0 if total <= 0, or -1 if impossible.
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    return dp[total] if dp[total] != total + 1 else -1
