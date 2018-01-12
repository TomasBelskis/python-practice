# -*- coding: utf-8 -*-
"""
Description: 1. Write a function to count how many odd numbers are in a list.

"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 1
@Description: Exercises 1
"""

def count_odd(l):
 count = 0
 for n in l:
     if (n % 2) != 0:
         count += 1
 return count

list_of_numbers = [10,3,4,5,9,12,34,55]

print(count_odd(list_of_numbers))
