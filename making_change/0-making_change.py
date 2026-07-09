#!/usr/bin/python3
"""
Main module for the makeChange function.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    
    Args:
        coins (list): A list of the values of the coins in possession.
        total (int): The target amount.
        
    Returns:
        int: Fewest number of coins needed, 0 if total <= 0, or -1 if impossible.
    """
    if total <= 0:
        return 0

    # Initialize a DP array of size (total + 1) filled with float('inf')
    # dp[i] will store the minimum coins needed for total 'i'
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins are needed to make a total of 0
    dp[0] = 0

    # Iterate through all totals from 1 to the target total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total cannot be formed
    return dp[total] if dp[total] != float('inf') else -1
