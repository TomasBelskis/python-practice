# -*- coding: utf-8 -*-
"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 8
@Description: Exercise 3. Encapsulate
              1 fruit = "banana"
              2 count = 0
              3 for char in fruit:
              4     if char == "a":
              5         count += 1
              6 print(count)
              in a function named count_letters, and generalize it so that it
              accepts the string and the letter as arguments. Make the function
              return the number of characters, rather than print the answer.
              The caller should do the printing.
"""


def count_letters(s,c):
    count = 0
    for letter in s:
        if letter == c:
            count +=1
    return count


print(count_letters("banana", 'a'))
