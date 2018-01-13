# -*- coding: utf-8 -*-
"""
Description: 5. Sum all the elements in a list up to but not including the first even number.
                (Write your unit tests. What if there is no even number?)

"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 5
@Description: Exercises 5
"""
import unittest


def sum_up_to_even(l):
 sum = 0
 for n in l:
     if (n % 2) != 1:
         break
     sum += n

 return sum


# Test cases:
class TestingExamples(unittest.TestCase):
    def setUp(self):
        pass

    def test_all_evens(self):
        self.assertEqual(sum_up_to_even([2, 4, 6, 8]), 0)

    def test_all_odd(self):
        self.assertEqual(sum_up_to_even([3, 9, 13, 17]), 42)

    def test_even_and_odd(self):
        self.assertEqual(sum_up_to_even([3, 9, 4, 3]), 12)

    def tearDown(self):
        pass


list_of_numbers = [3, 4, 5, 9, 12, 34, 55]

print(sum_up_to_even(list_of_numbers))