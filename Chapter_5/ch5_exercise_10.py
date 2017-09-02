"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 5 exercise 10
@Description: Write a function find_hypot which, given the
              length of two sides of a right-angled triangle,
              returns the length of the hypotenuse.
              (Hint: x ** 0.5 will return the square root.)

"""

def find_hypot(s1, s2):
    sqr_s1 = s1 ** 2
    sqr_s2 = s2 ** 2
    c = (sqr_s1+sqr_s2) ** 0.5
    return c

print(find_hypot(10,11))