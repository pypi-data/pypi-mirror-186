"""
Name: nums.py
Author: Oliver B. Gaither
Date: 1/16/2023
Description: math functions
"""

import math # math.sqrt(x), math.floor(x),
import numpy as np # for calculating the dot product

MAXINT64 = (1 << 63) - 1
MININT64 = -(1 << 63)
MAXINT32 = (1 << 31) - 1
MININT32 = -(1 << 31)
MAXINT16 = (1 << 15) - 1
MININT16 = -(1 << 15)


def dec_weights(N, balanced=0):
    """
    computes decending weights
    :param N: number of values to be weighted
    :param balanced: 1 or 0. 1 for less balance
    :return: numpy array of weight percentages
    """
    series = [fibonacci((N + (not balanced)) - i) for i in range(N)]
    t = sum(series)  # precompute sum of series
    return np.array([series[i] / t for i in range(N)])  # vector of diminishing weights


def fibonacci(n):
    """
    fast doubling method for calculating
    the nth fibonacci number
    :param n: a non negative integer
    :return: the nth fibonacci number
    """
    a = 0
    b = 1
    for _ in range(n):
        (a, b) = (b, a + b)
    return a


def isprime(n):
    """return True or False whether a given number is prime"""
    if n == 2 or n == 3:
        return True
    if (n <= 1) or (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while (i * i) <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def next_prime(n):
    """
    find the next prime number that
    is larger than the given number n
    :param n: a number
    :return: the smallest prime number larger than n
    """
    n = n + 1
    while not isprime(n):
        n += 1
    return n


def factor(n: int):
    """returns list of prime factors of a given number"""
    n = abs(n)
    t = []
    p = 2
    while n > 1:
        if n % p == 0:
            t.append(p)
            n = n / p
        else:
            p = p + 1
    return t


def getprimes(n):
    """
    return a list of primes numbers up to n
    using sieve of eratosthenes
    :param n: an upperbound
    :return: list of numbers
    """
    if n <= 1:
        raise ValueError("getprimes() number must be greater than 1")
    t = [True for _ in range(n + 1)]
    # initially mark 0 and 1 as composite numbers
    t[0] = False
    t[1] = False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if t[i]:
            # go up the table by a jump of the given number and mark each as composite
            # as it is a multiple of the current number
            for j in range(i * i, n, i):
                t[j] = False
    
    # create a list of the indicies that are still marked as true in the table
    primes = []
    for i in range(n):
        primes += [i] if t[i] else []
    return primes


def divisors(n):
    """
    return list of all divisors for a given number n
    :param n: a number
    :return: iterable of all divisors of n
    """
    factors = [1, n]
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if (n % i == 0):
            factors.append(i)
            factors.append(n // i)
    return iter(sorted(factors))


def is_perfect_square(n):
    """
    return whether a given number is a perfect square or not
    :param n:
    :return:
    """
    if n < 0:
        return False
    x = 1
    y = n
    while (x + 1) < y:
        mid = (x + y) >> 1
        if (mid * mid) < n:
            x = mid
        else:
            y = mid
    return (x * x == n) or ((x + 1) * (x + 1) == n)
