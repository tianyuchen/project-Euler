# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1
to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

# Cause we know the pandigital number should be from 1 to 9, 9 digits. So it must be
# double-digit * three-digit = four-digit
# one-digit * four-digit = four-digit

# And number 1 can't be the single digit of multiplicand/multiplier

def is_pandigital(n):
    n = str(n)
    return len(n) == 9 and not '123456789'.strip(n)


def sum_pandigital_products():
    products = []
    for i in range(2, 100):
        for j in range(2, 10000):
            if is_pandigital(str(i) + str(j) + str(i * j)):
                products.append(i * j)
    return sum(list(set(products)))

print(sum_pandigital_products())
