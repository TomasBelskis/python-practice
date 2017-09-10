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

class test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(turn_clockwise("N"), "E")

    def test_2(self):
        self.assertEqual(turn_clockwise("W"), "N")

    def test_3(self):
        self.assertEqual(turn_clockwise(41), "None")

    def test_4(self):
        self.assertEqual(turn_clockwise("rubbish"), "None")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()



