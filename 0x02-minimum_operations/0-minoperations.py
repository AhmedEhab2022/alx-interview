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

    ans = minOperationsRec(n, 2, 1, 2, {})
    if ans == float('inf'):
        return 0

    return ans


def minOperationsRec(n, Hnum, HprevNum, opCount, memo):
    """
    Recursive function to calculate the fewest number of operations needed,
    with memoization to store results of previous computations.

    Args:
        n (int): The target number of 'H' characters.
        Hnum (int): Current number of 'H' characters.
        HprevNum (int): Number of 'H' characters in the last copy operation.
        opCount (int): Current count of operations.
        memo (dict): Dictionary to store previously computed results.

    Returns:
        int: Minimum number of operations required or float('inf')
        if not possible.
    """
    if Hnum == n:
        return opCount
    elif Hnum > n:
        return float('inf')

    key = (Hnum, HprevNum)

    if key in memo:
        return memo[key]

    op1 = minOperationsRec(n, Hnum + HprevNum, HprevNum, opCount + 1, memo)
    op2 = minOperationsRec(n, Hnum * 2, Hnum, opCount + 2, memo)

    memo[key] = min(op1, op2)
    return memo[key]
