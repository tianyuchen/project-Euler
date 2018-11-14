# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

coin = [1, 2, 5, 10, 20, 50, 100, 200]
objective = 200
ways = 0

for a in range(0, objective / 200 + 1):
    objective -= a * 200
    print(a, objective)

    for b in range(0, objective / 100 + 1):
        objective -= b * 100
        for c in range(0, objective / 50 + 1):
            objective -= c * 50
            for d in range(0, objective / 20 + 1):
                objective -= d * 20
                for e in range(0, objective / 10 + 1):
                    objective -= e * 10
                    for f in range(0, objective / 5 + 1):
                        objective -= f * 5
                        for g in range(0, objective / 2 + 1):
                            objective -= g * 2
                            if objective >= 0:
                                print(a, b, c, d, e, f, g)
                                ways += 1
print(ways)
