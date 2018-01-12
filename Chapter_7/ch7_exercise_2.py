# -*- coding: utf-8 -*-
"""
Description: 2. Sum up all the even numbers in a list.

"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 2
@Description: Exercises 2
"""

def sum_even(l):
 sum = 0
 for n in l:
     if (n % 2) == 1:
         sum += n
 return sum

list_of_numbers = [10,3,4,5,9,12,34,55]

print(sum_even(list_of_numbers))
