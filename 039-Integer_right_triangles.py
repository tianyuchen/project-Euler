# -*- coding: utf-8 -*-
'''
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

# right angle triangle 直角三角形
# a^2 + b^2 = c^2
# a + b + c = p <= 1000
# a + b > c

# From c = p - a - b and  a^2 + b^2 = c^2, we can obtain b = p(2a -p)/2(a-p)
# Assume that a <= b < c so 3a < p, a < p/3

max_solutions = 0
max_p = 0

for p in range(2, 1001):
    nb_solutions = 0
    for a in range(2, p / 3):
        if (p * (2 * a -p)) % (2 * (a - p)) == 0:
            nb_solutions += 1
    if nb_solutions > max_solutions:
        max_solutions = nb_solutions
        max_p = p

print(max_p)
