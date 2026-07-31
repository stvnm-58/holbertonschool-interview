#!/usr/bin/python3
"""Prime game module."""


def isWinner(x, nums):
    """Determine the winner of the Prime Game across multiple rounds.

    Maria and Ben play a game where they take turns removing a prime number
    and all of its multiples from a set of consecutive integers starting from 
    1 up to a given number n. The player who cannot make a move loses the game.
    Maria always goes first, and both players play optimally.

    Args:
        x (int): The number of rounds to play.
        nums (list of int): A list containing the upper limit (n) for each round.

    Returns:
        str: The name of the player with the most wins ("Maria" or "Ben").
        None: If the total wins are tied or if the inputs are invalid.
    """
    if not nums or x <= 0:
        return None

    nums = nums[:x]
    n = max(nums)
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for multiple in range(i * i, n + 1, i):
                sieve[multiple] = False

    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if sieve[i]:
            count += 1
        prime_count[i] = count

    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
