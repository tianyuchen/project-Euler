# -*- coding: utf-8 -*-
'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
import time

def factorial(n):
    # factorial of zero is 1
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# 9! = 362880 has six digits. So if a number has '9' inside it, in order to have
# sum of factorials equals the number, the max limit need to be a 6 digit number.
# 6 * 9! = 2177280 has 7 digits. So the upper limit should be 7 * 9! = 2540160.
total = 0
start = time.time()

# cache the factorials
factorials = [factorial(i) for i in range(0, 10)]

for num in range(3, 2540161):
    sum = 0
    for i in str(num):
        sum += factorials[int(i)]
    if num == sum:
        total += num

elapsed_time = time.time() - start

print "Found %d in %r s." % (total, elapsed_time)
