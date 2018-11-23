# -*- coding: utf-8 -*-
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def is_prime(n):
    if n <= 1:
        return False
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n ** .5) + 1):
            if n % i == 0:
                return False
    return True

print(is_prime(18))
