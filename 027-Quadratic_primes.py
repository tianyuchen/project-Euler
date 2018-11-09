# -*- coding: utf-8 -*-
'''
  Quadratic primes
  Problem 27

  Euler discovered the remarkable quadratic formula:

  n² + n + 41

  It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.

  However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly divisible by 41.

  The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

  Considering quadratics of the form:

  n² + an + b, where |a| < 1000 and |b| < 1000

  where |n| is the modulus/absolute value of n
  e.g. |11| = 11 and |−4| = 4
  Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

'''
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

def primeRange(n):
  prime_lst = []
  for i in range(2, n):
    if isPrime(i):
      prime_lst.append(i)
  return prime_lst

def testEquation(a, b):
    n = 0
    while True:
        num = n ** 2 + a * n + b
        if isPrime(num): n += 1
        else: break
    return n

# b has to be prime
# The problem requires our n to start at 0, so our first result from a quadratic
# equation would be 0 + 0 + b = b. So b has to be positive, prime and less than 1000 (for this problem) which helps reduce the search space significantly.
max = 0
prime_under_1000 = primeRange(1000)
for a in range(-999, 1000):
  for b in prime_under_1000:
    n = testEquation(a, b)
    if n > max:
      max = n
      max_a = a
      max_b =b
print(max_a * max_b)
