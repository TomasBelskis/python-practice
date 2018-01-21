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


def find(strng, ch, n):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


def count_letters(s, c, n=False):
    count = 0
    for letter in s:
        indx = find(s, c, n)
        if indx != -1:
            count +=1

    return count


print(count_letters("banana", 'a'))