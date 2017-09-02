"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 5 exercise 12
@Description: Extend the above program so that the sides can be
              given to the function in any order.
"""

def is_rightangled(s1,s2,s3):
    sqr_s1 = s1 ** 2
    sqr_s2 = s2 ** 2
    sqr_s3 = s3 ** 2

    if (abs((sqr_s1 + sqr_s2) - sqr_s3) < 0.000001):
        return True
    else:
        return False

print(is_rightangled(3,4,5))
