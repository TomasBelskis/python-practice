# -*- coding: utf-8 -*-
"""
Description: 9. Write a function print_triangular_numbers(n) that prints
             out the first n tri- angular numbers.
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 9
@Description: Exercises 9
"""

def print_triangular_numbers(x):
        for i in range(1,x):
            tr = int(i*(i+1)/2)
            print(i,"   ",tr)

print_triangular_numbers(6)