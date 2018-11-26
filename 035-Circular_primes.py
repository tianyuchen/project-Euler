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

def rotation(N):
    # ex. N[i:] = [1, 9, 7], [9, 7], [7]  N[:i] = [], [1], [1, 9]
    rot = []
    for i in range(len(N)):
        rot.append(N[i:] + N[:i])
    for num in rot:
        res = ''.join(str(num))
        print(res)
    # return [N[i:] + N[:i] for i in range(len(N))]
    return res

def circular_primes(n):
    K = []
    for i in str(n):
        K.append(i)
    return rotation(K)

print(circular_primes(197))
