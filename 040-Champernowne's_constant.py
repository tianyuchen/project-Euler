# -*- coding: utf-8 -*-
'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''


# 1 ~ 9         9 digits
# 10 ~ 99       2 * (99 - 10 + 1) = 180 digits
# 100 ~ 999     3 * 900 = 2700 digits
# 1000 ~ 9999   4 * 9000 = 36000 digits
# 10000 ~ 99999 5 * 90000 = 450000 digits


# d1 = 1
# d10 = (10 - 9) / 2 = 0.5 --> first digit of (9 + 1)th number = 1
# d100 = (100 - 9) / 2 =  45.5 --> first digit of (9 + 46)th number = 5
# d1000 = (1000 - 9 - 180) / 3 = 270 ... 1 --> first digit of (99 + 271)th number = 3

digits = [(x + 1) * 9 * pow(10, x) for x in range(0, 6)]

def d(n):
    i = 0
    if n < 9:
        return n
    while n > digits[i]:
        n -= digits[i]
        i += 1
    quotient, remainder = divmod(n , i + 1)
    return int(str(pow(10, i) + quotient)[remainder - 1])

produit = 1
for i in range(0, 7):
    produit *= d(pow(10, i))
print(produit)
