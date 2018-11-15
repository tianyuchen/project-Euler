# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# Solution 1

ways = 0
reste = 200

for a in range(0, reste + 1, 200):
    reste = 200 -a
    for b in range(0, reste + 1, 100):
        reste = 200 - a - b
        for c in range(0, reste + 1, 50):
             reste = 200 - a - b - c
             for d in range(0, reste + 1, 20):
                 reste = 200 - a - b - c - d
                 for e in range(0, reste + 1, 10):
                     reste = 200 - a - b - c - d - e
                     for f in range(0, reste + 1, 5):
                         reste = 200 - a - b - c - d - e - f
                         for g in range(0, reste + 1, 2):
                             h = 200 - a - b - c - d - e - f - g
                             if h >= 0:
                                 ways += 1
print(ways)


# Solution 2: dynamic programming

target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0] * target

for coin in coins:
    for i in range(coin, target + 1):
        ways[i] += ways[i - coin]

print(ways[target])
