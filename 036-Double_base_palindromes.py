# -*- coding: utf-8 -*-
'''
The decimal number, 585 = 1001001001(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

def is_palindromic(n):
    n = str(n)
    return n == n[::-1]

sum = 0
for i in range(1, 10 ** 6):
    # bin() will convert to binary with format like 0b11101
    binary_i = bin(i)[2:]

    if is_palindromic(i) and is_palindromic(binary_i):
        sum += i
print(sum)
