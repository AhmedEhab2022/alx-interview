#!/usr/bin/python3
""" Making Change """

def makeChange(coins, total):
	""" Given a pile of coins of different values, determine the fewest
		number of coins needed to meet a given amount total.
	"""
	if total <= 0:
		return 0

	n = len(coins)
	dp = [0]
	for _ in range(total):
		dp.append(total + 1)

	for i in range(1, total + 1):
		for j in coins:
			if j <= i:
				if dp[i - j] == total + 1 or dp[i - j] == -1:
					dp[i] = -1
					continue
				dp[i] = min(dp[i - j] + 1, dp[i])

	return dp[total]
