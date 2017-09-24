# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
# that the 6th prime is 13.
#
# What is the 10 001st prime number?

# -- RUN for 9s ---
# i = 3
# primelst = [2, 3]
# prime_count = 2
# while prime_count < 10001:
#     i += 2
#     for j in primelst:
#         if i % j != 0:
#             isprime = True
#         else:
#             isprime = False
#             break
#     if isprime:
#         primelst.append(i)
#         prime_count += 1
# print i


# --- Opimisation RUN for 0.3s---
def isPrime(num):
    if num <= 1:
        return False
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num ** .5) + 1):
            if num % i == 0:
                return False
    return True


def primes(n):
    # Returns a sorted list of first n prime numbers
    from itertools import count
    primes_list = []

    for i in count(1):  # Iterator: 1, 2, 3 ...
        if isPrime(i):
            primes_list.append(i)
        if len(primes_list) == n:
            return primes_list


print(primes(10001)[-1])  # index -1: last element of the list
