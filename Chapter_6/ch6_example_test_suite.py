# Unit Testing Python Code

"""
- Testing code is important, this can be done by writing test cases in order
to test functions.
"""

import sys

def absolute_value(x):
    if x < 0:
        return -x
    return x

def absolute_value_bug(n):# Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        return 1
    elif n > 0:
        return n

def test(did_pass):
    """ Print the result of the test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number
    if did_pass:
        msg = " Test at line {0} ok. ".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    """ Run the suite of test for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)
    # Testing buggy version of the function
    test(absolute_value_bug(17) == 17)
    test(absolute_value_bug(-17) == 17)
    test(absolute_value_bug(0) == 0)
    test(absolute_value_bug(3.14) == 3.14)
    test(absolute_value_bug(-3.14) == 3.14)

test_suite() # Here is the call to run the tests
# Tree test fail for the buggy version
# TODO Read up on assertion and how to use instead of writing own test function

