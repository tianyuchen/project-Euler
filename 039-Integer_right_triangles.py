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

# from c = p - a - b and  a^2 + b^2 = c^2, we can obtain b = p(2a -p)/2(a-p)

a ** 2 + b ** 2 == c ** 2
