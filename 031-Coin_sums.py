# -*- coding: utf-8 -*-
'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# Solution 1
def solution1():
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
    return ways



# Solution 2: recursive
# ex. coins = [1, 2, 5] ways[10] = ways[10 - 1] + ways[10 - 2] + ways[10 - 5]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
# Can be optimised with cache with (key = "(rest-coins[i])_i", result)
def solution2(rest, max_index):
    # All 200p have been taken, counts a new way
    if rest == 0:
        return 1
    if rest < 0:
        return 0

    total = 0
    for i in range(max_index, -1, -1):
        total += way(rest - coins[i], i)
    return total

print(solution2(200, len(coins) - 1))


# Solution 3: dynamic programming
# ways[200] = ways[200-1] + ways[200-2] + ways[200-5] + ways[200-10] + ...
# ways[2] = ways[1] = 1
# ways[3] = ways[2] + ways[1] = 2
# ways[4] = ways[3] + ways[2] = 3
# ways[5] = ways[4] + ways[3] = 5
# ways[6] = ways[5] + ways[4] + ways[1] = 9

def solution3():
    target = 200
    ways = [1] + [0] * target

    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
    return ways[target]
