# -*- coding: utf-8 -*-
'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct,
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than
one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find
the value of the denominator.
'''

# Four non-trivial cases：
# 1.  ab/cb = a/c    2. ba/bc = a/c    3. ba/cb = a/c   4. ab/bc = a/c
# Cause the fraction is less than one, a/c < 1. After simplification case 1 and
# case 2 => a = c, don't match  a < c. equation 3 doen't have a solution as well.
# So only fraction ab/bc = a/c left

# (10a + b) / (10b + c) = a / c
# 10ac + bc = 10ab + ac
# 9a * (c - b) = b * (a - c)
# a < c < b <= 9

from fractions import gcd

prod_numerator = 1
prod_denominator = 1
for b in xrange(1, 10):
    for c in xrange(1, b):
        a, r = divmod(b * c, 10 * b - 9 * c)
        if not r and a <= 9:
            prod_numerator *= a
            prod_denominator *= c

# miinimalist denominator is the prod_denominator divise by its highest common factor
prod_denominator /= gcd(prod_numerator, prod_denominator)

print(prod_denominator)
