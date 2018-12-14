# -*- coding: utf-8 -*-
'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of
each of the digits 0 to 9 in some order, but it also has a rather interesting
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note
the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''

import itertools

primes = [2, 3, 5, 7, 11, 13, 17]


def is_sub_string_divisible(n):
    for i in range(1, 8):
        if int(str(n)[i: i + 3]) % primes[i - 1] != 0:
            return False
    return True


def sum_of_divisible_pandigital_numbers():
    sum = 0
    pandigital_nums = [int(''.join(item)) for item in itertools.permutations("0123456789")]
    for num in pandigital_nums:
        if is_sub_string_divisible(num):
            sum += num
    return sum


print(sum_of_divisible_pandigital_numbers())
