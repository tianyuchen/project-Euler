# -*- coding: utf-8 -*-
'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0 or n < 2:
        return False
    else:
        # only odd numbers
        for i in range(3, int(n ** .5) + 1, 2):
            if n % i == 0:
                return False
    return True


def rotation(n):
    N = []
    rot = []
    res = []
    # from number to list
    for i in str(n):
        N.append(i)

    # all rotations of number of separate digits
    for i in range(len(N)):
        # ex. N[i:] = [1, 9, 7], [9, 7], [7]  N[:i] = [], [1], [1, 9]
        rot.append(N[i:] + N[:i])

    # join separate digits to number
    for num in rot:
        res.append(int(''.join(str(digit) for digit in num)))
    return res


def circular_primes(n):
    total = 0
    for i in range(2, 10 ** n):
        for num in rotation(i):
            if(is_prime(num)):
                circular_prime = True
            else:
                circular_prime = False
                break
                
        if circular_prime:
            total += 1
    return total

print(circular_primes(6))
