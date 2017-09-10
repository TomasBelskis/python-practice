# -*- coding: utf-8 -*-
"""
Condition: All of the exercises below should be added to a single file. In
           that file, you should also add the test and test_suite scaffolding
           functions shown above, and then, as you work through the exercise-
           s, add the new tests to your test suite. (If you open the online
           version of the textbook, you can easily copy and paste the tests
           and the fragments of code into your Python editor.)

"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 6 exercise 1-19
@Description: Exercises 1-19 for chapter 6
"""

import unittest

def turn_clockwise(direction):


    if direction == "N":
        return  "E"
    elif direction == "E":
        return  "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return  "N"
    else:
        return "None"
    return "None"

def day_name(num):
    return "None"

class test(unittest.TestCase):
    def setUp(self):
        pass
    """
        Exercise 1:The four compass points can be abbreviated by single-lett-
        er strings as “N”, “E”, “S”, and “W”. Write a function turn_clockwise
        that takes one of these four compass points as its parameter, and re-
        turns the next compass point in the clockwise direction. Here are so-
        me tests that should pass:
    """
    def test_1(self):
        self.assertEqual(turn_clockwise("N"), "E")

    def test_2(self):
        self.assertEqual(turn_clockwise("W"), "N")

    def test_3(self):
        self.assertEqual(turn_clockwise(41), "None")

    def test_4(self):
        self.assertEqual(turn_clockwise("rubbish"), "None")

    """End Exercise 1 test"""

    """
        Exercise 2: Write a function day_name that converts an integer number
        0 to 6 into the name of a day. Assume day 0 is “Sunday”. Once again, 
        return None if the arguments to the function are not valid. Here are 
        some tests that should pass:
    """
    def test_1_day(self):
        self.assertEqual(day_name(3), "Wednesday")

    def test_2_day(self):
        self.assertEqual(day_name(6), "Saturday")

    def test_3_day(self):
        self.assertEqual(day_name(42), "None")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()



