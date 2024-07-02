#!/usr/bin/python3
""" Prime Game """


def sieveOfEratosthenes(n):
    """
    Return: Boolean list of length n,
    when the index is prime the value is True, False otherwise

    Args:
        n: the end number
    """
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False
    return prime


def isWinner(x, nums):
    """
    Return: name of the player that won the most rounds (Maria / Ben)

    Args:
        x:  the number of rounds
        nums: is an array of n
    """
    mariaRounds = benRounds = 0
    for round in range(x):
        n = nums[round]
        primes = sieveOfEratosthenes(n)
        primesCount = 0
        for prime in primes:
            if prime:
                primesCount += 1

        if primesCount % 2:
            mariaRounds += 1
        else:
            benRounds += 1

    if mariaRounds > benRounds:
        return "Maria"
    if mariaRounds < benRounds:
        return "Ben"

    return None
