"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 5 exercise 12
@Description: Extend the above program so that the sides can be
              given to the function in any order.
"""
# TODO rewrite the if statements, determine max value using max function
def is_rightangled(s1,s2,s3):
    sqr_s1 = s1 ** 2
    sqr_s2 = s2 ** 2
    sqr_s3 = s3 ** 2

    if (s3 > s2 > s1):
        if (abs((sqr_s1 + sqr_s2) - sqr_s3) < 0.000001):
            return True
        else:
            return False
    elif (s2 > s3 > s1):
        if (abs((sqr_s1 + sqr_s3) - sqr_s2) < 0.000001):
            return True
        else:
            return False
    else:
        if (abs((sqr_s2 + sqr_s3) - sqr_s1) < 0.000001):
            return True
        else:
            return False

print(is_rightangled(6,4,3))
