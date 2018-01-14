# -*- coding: utf-8 -*-
"""
Description: 15. Write a function num_even_digits(n) that counts the number
                 of even digits in n. These tests should pass:
                 test(num_even_digits(123456) == 3)
                 test(num_even_digits(2468) == 4)
                 test(num_even_digits(1357) == 0)
                 test(num_even_digits(0) == 1)
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 15
@Description: Exercises 15
"""
import unittest

def num_even_digits(n):
    count = 0
    if n == 0: return 1
    while n != 0:
        if n % 2 == 0:
            count += 1
        n = n // 10

    return count


# Test cases:
class TestingExamples(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(num_even_digits(123456), 3)

    def test_2(self):
        self.assertEqual(num_even_digits(2468), 4)

    def test_3(self):
        self.assertEqual(num_even_digits(1357), 0)

    def test_4(self):
        self.assertEqual(num_even_digits(0), 1)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()