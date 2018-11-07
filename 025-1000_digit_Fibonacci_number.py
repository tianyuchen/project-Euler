# -*- coding: utf-8 -*-
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


# First solution
import math

list_Fib = [1, 1]
next_item = 2
index = 0

# The 'result' of log10(number) can define 'number' contain ('result' + 1) digits
# So when log10('next_item') = 999, next_item is the first number contains 1000 digits
while math.log10(next_item) < 999:
    next_item = list_Fib[len(list_Fib)-2] + list_Fib[len(list_Fib)-1]
    list_Fib.append(next_item)
print(len(list_Fib))


# Seconde solution
a = 1
b = 1
resultat = 2
while len(str(b)) < 1000:
    # This way to calculate Fibonacci sequence is more effective, without save entire
    # Fibonacci sequence and without using intermediate number
    a, b = b, a+b
    resultat += 1
print(resultat)
