# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is  if it makes use of all the digits
1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import itertools

def pandigital_numbers(n):
    # Generate list of number 1 to n.  ex: '1234'
    list_num = ''.join([str(i) for i in range(1, n + 1)])

    # List all pandigital numbers of digits 1 to n
    pandigital_str = [''.join(item) for item in itertools.permutations(list_num)]
    # transfer pendigital number from string to int
    pandigital_num = [int(num) for num in pandigital_str]
    pandigital_num.sort(reverse=True)
    return pandigital_num

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# An integer is divisible by 3 whose sum of digits is divisible by 3 and therefore composite and not prime.
#
# 9+8+7+6+5+4+3+2+1+0 = 45, 45/3 = 15
# 9+8+7+6+5+4+3+2+1 = 45, 45/3 = 15
# 8+7+6+5+4+3+2+1 = 36, 36/3 = 12
# 7+6+5+4+3+2+1 = 28, 28/3 = 9.333…

# So the largest pandigital prime should be an 7-digit number

def largest_pandigital_prime():
    # for i in range(9, 0, -1):
    for num in pandigital_numbers(7):
        if is_prime(num):
            return num

print(largest_pandigital_prime())
