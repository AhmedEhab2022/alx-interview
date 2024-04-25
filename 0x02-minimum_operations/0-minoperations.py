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
    elif n == 2:
        return 2

    ans = minOperationsRec(n, 2, 1, 2)
    if ans == float('inf'):
        return 0

    return ans


def minOperationsRec(n, Hnum, HprevNum, opCount):
    """
    Recursive function to calculate the fewest number of operations needed.
    """
    if Hnum == n:
        return opCount
    elif Hnum > n:
        return float('inf')

    x = minOperationsRec(n, Hnum + HprevNum, HprevNum, opCount + 1)
    y = minOperationsRec(n, Hnum * 2, Hnum, opCount + 2)

    return min(x, y)
