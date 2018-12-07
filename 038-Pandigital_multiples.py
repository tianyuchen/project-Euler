# -*- coding: utf-8 -*-
'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will
call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5,
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def is_pandigital(n):
    n = str(n)
    # strip() will delete chars n from string
    # When n is pandigital, '123456789'.strip(n) should be '' is considered to be False
    return len(n) == 9 and not '123456789'.strip(n)

# Max pandigital must begin with 9 and it should be >= 918273645.
# 92 ~ 98 don't satisfaited the condition because when it multiplied by (2, 3, 4),
# they can’t make a 9-digit concatenated product. (2+3+3+3...)
# 921 ~ 987 multiplied by (2, 3, 4) can’t make a 9-digit concatenated product.  (3+4+4+...)
# 9213 ~ 9876 multiplied by (2, 3, 4) can make a 9-digit concatenated product.  (4+5)
# other combinations will create too many digits.


list = [str(i) + str(i * 2) for i in range(9213, 9877) if is_pandigital(str(i) + str(i * 2))]

print list[-1]
