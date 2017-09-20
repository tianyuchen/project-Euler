# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible(divisible with
# no remainder) by all of the numbers from 1 to 20?

from fractions import gcd
from functools import reduce


def lcm(a, b):
    # calculate the lowest common multiple of two integers a and b
    # formule: gcd(a,b) * lcm(a,b) = a * b with gcd: greatest common divisor
    return a * b//gcd(a, b)


def smallest_multiple():
    # reduce(function, iterable[, initializer])
    # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
    return reduce(lcm, range(1, 21))


print smallest_multiple()
