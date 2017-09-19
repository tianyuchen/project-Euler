# A palindromic number reads the same both ways.
# The smallest 6 digit palindrome made from the product of two 3-digit numbers
# is 101101 = 143 * 707.
#
# Find the largest palindrome made from the product of two 3-digit numbers
# which is less than N


def largest_palindrome_product(val):
    # max(a,b,c,key=func)
    num = max(i * j
            for i in range(100, 1000)
            for j in range(100, 1000)
            # check if palindrome, turning the number into a string,
            # using slice notation to reverse the string
            if str(i * j) == str(i * j)[::-1] and i * j < val)
    print num


largest_palindrome_product(800000)
