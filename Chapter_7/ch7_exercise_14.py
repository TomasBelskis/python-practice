# -*- coding: utf-8 -*-
"""
Description: 14. What will num_digits(0) return? Modify it to return
                 1 for this case. Why does a call to num_digits(-24)
                 result in an infinite loop? (hint: -1//10 evaluates
                 to -1) Modify num_digits so that it works correctly
                 with any integer value. Add these tests:
                  test(num_digits(0) == 1)
                  test(num_digits(-12345) == 5)
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 14
@Description: Exercises 14
"""
import unittest
import math



def num_digits(n):
    count = 0
    if n == 0:
        return 1

    while n != 0:
        count = count + 1
        n = round(math.fabs(n // 10))
    return count


# Test cases:
class TestingExamples(unittest.TestCase):
    def setUp(self):
        pass

    def test1(self):
        self.assertEqual(num_digits(0), 1)

    def test2(self):
        self.assertEqual(num_digits(-12345), 5)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()