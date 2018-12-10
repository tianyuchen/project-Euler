# -*- coding: utf-8 -*-
'''
We shall say that an n-digit number is  if it makes use of all the digits
1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
import itertools

<<<<<<< HEAD
def pandigital_numbers(n):
    # Generate list of number 1 to n.  ex: '1234'
    list_num = ''.join([str(i) for i in range(1, n + 1)])

    # List all pandigital numbers of digits 1 to n
    pandigital_str = [''.join(item) for item in itertools.permutations(list_num)]
    # transfer pendigital number from string to int
    pandigital_num = [int(num) for num in pandigital_str]
    pandigital_num.sort(reverse=True)
    return pandigital_num
=======
def pandigital(n):
    list_num = ''.join(i) for i in range(1, 4)
    print(list_num)
    # join the permutation lists into single numbers by joining each into a string
    nums = [''.join(item) for item in itertools.permutations(n)]
    print(nums)


>>>>>>> 5d32990c3373d01b3fcb3d0b07017cd6110e9c42

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

<<<<<<< HEAD
def largest_pandigital_prime():
    for i in range(9, 0, -1):
        for num in pandigital_numbers(i):
            if is_prime(num):
                return num

print(largest_pandigital_prime())
=======
print(pandigital('123'))
>>>>>>> 5d32990c3373d01b3fcb3d0b07017cd6110e9c42
