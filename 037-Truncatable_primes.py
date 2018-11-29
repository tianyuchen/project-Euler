# -*- coding: utf-8 -*-
'''
The number 3797 has an interesting property. Being prime itself, it is possible
to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


sum = 0
nb_primes = 0
truncatable_prime = None
for n in range(9, 10 ** 6, 2):
    for i in range(0, len(str(n))):
        # Test if n is prime both truncatable from left to right and right to left
        if not is_prime(int(str(n)[i : ])) or not is_prime(int(str(n)[: i + 1])):
            truncatable_prime = False
            break
        truncatable_prime = True

    if truncatable_prime == True:
        nb_primes += 1
        sum += n
    # when we have first eleven primes, stop the program
    if nb_primes == 11:
        print(sum)
        break
