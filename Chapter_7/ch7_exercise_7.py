# -*- coding: utf-8 -*-
"""
Description: 7. Add a print function to Newton’s sqrt function that prints
                out better each time it is calculated. Call your modified
                function with 25 as an argument and record the results.
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 7
@Description: Exercises 7
"""

def sqrt(n):
    approx = n/2.0  # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print("Better is: ", better)
        if abs(approx - better) < 0.001:
            return better
        approx = better

sqrt(25)