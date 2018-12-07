# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is  if it makes use of all the digits
1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

def pandigital(n):
    # list_num = [i for i in range(1, n+1)]
    # join the permutation lists into single numbers by joining each into a string
    nums = [''.join(item) for item in itertools.permutations(n)]

    print(nums)


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(pandigital(4))
