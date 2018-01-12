# -*- coding: utf-8 -*-
"""
Description: 6. Count how many words occur in a list up to and including the first occurrence
                of the word “sam”. (Write your unit tests for this case too. What if “sam”
                does not occur?)
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 6
@Description: Exercises 6
"""
import unittest


def count_words(wl):
 count = 0
 for w in wl:
     count += 1
     if w == "sam":
         break
 return count


# Test cases:
class TestingExamples(unittest.TestCase):
    def setUp(self):
        pass

    def test_normal_case(self):
        self.assertEqual(count_words(["hero","car","yes","sam","no","tennis"]),4)

    def test_no_sam(self):
        self.assertEqual(count_words(["hero","cat","dog"]),3)

    def tearDown(self):
        pass

list_of_words = ["hero","war","sam","monkey"]

print(count_words(list_of_words))