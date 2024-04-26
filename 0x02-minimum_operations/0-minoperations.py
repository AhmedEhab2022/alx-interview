#!/usr/bin/python3
"""
This module contains the minOperations function
"""


def minOperations(n):
    """
    Method that calculates the fewest number of operations needed to
    result in exactly n H characters in the file.

    Args:
        n (int): The number of characters to be printed.

    Returns:
        int: The fewest number of operations needed to
        result in exactly n H characters in the file
        or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    dp = [0] * (n + 1)
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = i
        for j in range(i - 1, 1, -1):
            if i % j == 0:
                dp[i] = dp[j] + i // j
                break

    return dp[n]
