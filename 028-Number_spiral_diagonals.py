# -*- coding: utf-8 -*-
'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5
spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# 1 (3 5 7 9) (13 17 21 25) (31 37 43 49)
# The difference between 1st and 5th diagonal number is 2, the difference between
# 5th and 9th is 4, the difference between 9th and 13th is 6.

def sum_of_diagonals(n):
    res = num = 1
    # The difference between number in a circle is 2, 4, 6, 8 ...
    for i in range(2, n, 2):
        # The circle of 4 numbers
        for j in range(4):
            num += i
            res += num
    return res

print(sum_of_diagonals(1001))
