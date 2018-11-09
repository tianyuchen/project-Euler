# A unit fraction contains 1 in the numerator. The decimal representation of the unit
# fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen
# that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in
# its decimal fraction part.

import math

def recurring_cycle_digits(n):
    digits = []
    remainder = 1
    # Zero is the number impossoble to become quotient
    quotient = 0
    cycle_len = 0
    digitLength = int(math.log10(n)) + 1

    while quotient not in digits and remainder != 0:
        digits.append(quotient)
        quotient, remainder = divmod((10 ** digitLength) * remainder, n)

    if quotient in digits:
        digits.pop(0)
        # '- digits.index(quotient)' for the case when repeating after a non-repeating part
        cycle_len = len(digits) - digits.index(quotient)
    return cycle_len

maxValue = 0
for i in range(2, 1000):
    if recurring_cycle_digits(i) > maxValue:
        maxValue = recurring_cycle_digits(i)
        maxIndex = i

print(maxIndex)
