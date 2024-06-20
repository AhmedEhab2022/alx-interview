#!/usr/bin/python3
""" Making Change """


def makeChange(coins, total):
    """ Given a pile of coins of different values, determine the fewest
        number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    dp = [total + 1 for k in range(total + 1)]
    dp[0] = 0
    for i in range(1, total + 1):
        for j in coins:
            if j <= i:
                if dp[i - j] == total + 1 or dp[i - j] == -1:
                    dp[i] = -1
                    continue
                dp[i] = min(dp[i - j] + 1, dp[i])

    return dp[total]
