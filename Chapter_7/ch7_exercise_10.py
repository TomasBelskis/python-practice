# -*- coding: utf-8 -*-
"""
Description: 10. Write a function, is_prime, which takes a single integer
             argument and returns True when the argument is a prime number
             and False otherwise. Add tests for cases like this:

             The last case could represent your birth date. Were you born on
             a prime day? In a class of 100 students, how many do you think
             would have prime birth dates?
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 10
@Description: Exercises 10
"""

import unittest

def is_prime(n):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                return False
            else:
                return True
        return False


# Test cases:
class TestingExamples(unittest.TestCase):
    def setUp(self):
        pass

    def test_isPrime_1(self):
        self.assertTrue(is_prime(11))

    def test_notPrime_1(self):
        self.assertFalse(is_prime(35))

    def test_isPrime_2(self):
        self.assertTrue(is_prime(19911121))

    def tearDown(self):
        pass


print(is_prime(19071993))
