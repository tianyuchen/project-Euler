# -*- coding: utf-8 -*-
'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so
the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value. For example, the word value
for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then
we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file
containing nearly two-thousand common English words, how many are triangle words?
'''

# x = ½n(n+1) -> in order to test if a number is triangle number, we need to verify
# n is a integer
# 8 * x + 1 = (2 * n + 1) ** 2

def is_triangle(x):
    if ((8 * x + 1) ** 0.5 - 1) % 2 == 0:
        return True
    return False


def word_alphabetical_value(word):
    value = 0
    for character in word.lower():
        # 96 == ord('a')
        position = ord(character) - 96
        value += position
    return value


def sum_triangle_words():
    total = 0
    for word in open('042_words.txt').read().replace('"', '').split(','):
        if is_triangle(word_alphabetical_value(word)):
            total += 1
    return total

print(sum_triangle_words())
