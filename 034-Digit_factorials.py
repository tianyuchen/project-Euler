# -*- coding: utf-8 -*-
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

def factorial(n):
    if n == 1 or n == 0:
        return n
    else:
        return n * factorial(n - 1)


for num in range(3, 1000):
    sum = 0
    for i in str(num):
        sum += factorial(int(i))
    if num == sum:
        print(num)
