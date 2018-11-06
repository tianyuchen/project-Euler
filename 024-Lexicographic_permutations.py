# A permutation is an ordered arrangement of objects. For example, 3124 is one
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
# are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# digits = [0, 1, 2]
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)

print(factorial(len(digits))) # 3628800
print(factorial(len(digits) - 1)) # 362880

# 9! = 362880 < 1000000 (th lexicographic permutation) < 10! = 3628800
n = 9

# def permutations(digits):
while n > 0:
    tmp = divmod(10**6, factorial(n))
    print(tmp)
    #the next digit is the number of times 'n!' fits into 'objective'
    answer += str(digits[tmp[0]])
    #the new 'objective' becomes 'objective mod n!'
    objective = tmp[1]
    n -= 1
    #don't use a digit twice
    digits.remove(digits[tmp[0]])
answer += str(digits[0])
print(answer)

# permutations(digits)
