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
# 1.  ab/cb = a/c    2. ba/bc = a/c    3. ab/bc = a/c   4. ba/cb = a/c
# Cause the fraction is less than one, a/c < 1. After simplification case 1 and
# case 2 => a = c, don't match  a < c.

d = 1
for i in xrange(1, 10):
    for j in xrange(1, i):
        q, r = divmod(9*j*i, 10*j-i)
        if not r and q <= 9:
            d*= i/float(j)
