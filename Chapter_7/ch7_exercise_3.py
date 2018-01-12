# -*- coding: utf-8 -*-
"""
Description: 3. Sum up all the negative numbers in a list.

"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 3
@Description: Exercises 3
"""

def sum_negative(l):
 sum = 0
 for n in l:
     if n < 0:
         sum += n
 return sum

list_of_numbers = [10,3,-4,5,9,-12,34,55]

print(sum_negative(list_of_numbers))
