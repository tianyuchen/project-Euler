# -*- coding: utf-8 -*-
'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

# To determine the upper bound, the fifth powers of the max single digit is 9 ^ 5 = 59049,
# since it's a 5 digits number, so 5 * 9 ^ 5 = 295245,  with 5 digits we can make a 6 digit number.
# 6*95 = 354294. So 355000 seems like a reasonable upper bound to use.
