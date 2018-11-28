# -*- coding: utf-8 -*-
'''
The decimal number, 585 = 1001001001(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

sum = 0
for i in range(1, 10 ** 6):
    # bin() will convert to binary with format like 0b11101
    binary_i = bin(i)[2:]

    if str(i) == str(i)[::-1] and str(binary_i) == str(binary_i)[::-1]:
        sum += i
print(sum)
