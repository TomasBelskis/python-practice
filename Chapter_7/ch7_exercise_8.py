# -*- coding: utf-8 -*-
"""
Description: 8. Trace the execution of the last version of
                print_mult_table and figure out how it works.
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 8
@Description: Exercises 8
"""


def print_multiples_r(n, high):
    for i in range(1, high + 1):
        print(n * i, end="   ")
    print()

def print_mult_table_r(high):
    for i in range(1, high + 1):
        print_multiples_r(i, high)


print_mult_table_r(5)