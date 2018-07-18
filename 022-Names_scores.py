#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a
# name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN
# would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

def alphabeticalValue(name):
    value = 0
    for character in name.lower():
        position = ord(character) - 96
        value += position
    return value

def nameScore():
    sum = 0
    with open('022_names.txt') as f:
        content = f.readlines()
        for line in content:
            names = line.replace('"', '').split(',')
            names.sort()
    for name in names:
        sum += alphabeticalValue(name) * (names.index(name) + 1)

    return sum

print(nameScore())
