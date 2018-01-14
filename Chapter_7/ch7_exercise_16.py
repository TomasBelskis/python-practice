# -*- coding: utf-8 -*-
"""
Description: 16. Write a function sum_of_squares(xs) that computes
                 the sum of the squares of the numbers in the list xs.For example,
                 sum_of_squares([2, 3, 4]) should return 4+9+16 which is 29:
                  test(sum_of_squares([2, 3, 4]) == 29)
                  test(sum_of_squares([ ]) == 0)
                  test(sum_of_squares([2, -3, 4]) == 29)
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 16
@Description: Exercises 16
"""

import unittest


def sum_of_squares(xs):
    total_sum = 0
    for x in xs:
        total_sum += x * x

    return total_sum


# Test cases:
class TestingExamples(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(sum_of_squares([2, 3, 4]), 29)

    def test_2(self):
        self.assertEqual(sum_of_squares([]), 0)

    def test_3(self):
        self.assertEqual(sum_of_squares([2, -3, 4]), 29)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()