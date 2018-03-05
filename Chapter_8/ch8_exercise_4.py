# -*- coding: utf-8 -*-
"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 8
@Description: Exercise 4. Now rewrite the count_letters function so that instead
                          of traversing the string, it repeatedly calls the find
                          method, with the optional third parameter to locate
                          new occurrences of the letter being counted.
"""


def find(strng, ch, ix=0):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


def count_letters(s, c):
    count = 0
    index = 0
    while index != -1:
        index = find(s, c, index)
        if index == -1: break
        index += 1 # if index is not = -1 increment the index to search from next letter.
        count += 1 # increment the count of letters found in a string

    return count


print(count_letters("banana", 'a'))