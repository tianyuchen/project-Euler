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

factorial(len(digits))   # 10! = 3628800
factorial(len(digits) - 1)   # 9! = 362880, ex. when first digit is zero, there are 9! permutations

# 2 * 9! < 1000000 (th lexicographic permutation) < 3 * 9! so the first number is 2
n = 9
objective = 10 ** 6
answer = ""

while n > 0:
    tmp = divmod(objective, factorial(n))
    # the next digit is the round number of objective divide by n!
    answer += str(digits[tmp[0]])
    # the remainder becomes new objective
    objective = tmp[1]
    n -= 1
    # delete used digit
    digits.remove(digits[tmp[0]])
# add the last digit
answer += str(digits[0])
print(answer)
