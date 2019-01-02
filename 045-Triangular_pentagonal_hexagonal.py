# -*- coding: utf-8 -*-
'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''
# Hexagonal numbers are a subset of Triangle number
# n = 2m – 1 Tn = (2m -1)((2m-1) 1)/2 = (2m-1)2m/2 = m(2m-1)

from math import sqrt

def is_pentagonal(n):
    num = (sqrt(24 * n + 1) + 1) / 6
    return num.is_integer()

# The first triangle, pentagonal, and hexagonal number is H143 = 40755.
i = 143

while True:
    i += 1
    n = i * (2 * i - 1)
    if(is_pentagonal(n)):
        print(n)
        break
