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

# TODO write comments for each function

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
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(len(days)):
        if i == num:
            return days[i]

    return "None"

def day_num(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(len(days)):
        if days[i] == day:
            return i

    return "None"

# TODO Finish of exercise 4 function
def day_add(day, num):
    s = 0
    leave_day = 0
    days = ["Monday","Tuesday","Wendnesday","Thursday","Friday","Saturday","Sunday"]
    for i in range(len(days)):
        if days[i] == day:
            s = i

    leave_day = s + (num % 7)

    if(leave_day < 7 ):
        return days[leave_day]
    else:
        leave_day = leave_day % 7
        return days[leave_day]

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
    """Exercise 2 END"""

    """
        Exercise 3: Write the inverse function day_num which is given a day 
        name, and returns its number:
    """
    def test_1_dayInverse(self):
        self.assertEqual(day_num("Friday"), 5)

    def test_2_dayInverse(self):
        self.assertEqual(day_num("Sunday"), 0)

    def test_3_dayInverse(self):
        self.assertEqual(day_num(day_name(3)), 3)

    def test_4_dayInverse(self):
        self.assertEqual(day_name(day_num("Thursday")), "Thursday")

    def test_5_dayInverse(self):
        self.assertEqual(day_num("Halloween"), "None")

    """
        Exercise 4: Write a function that helps answer questions like “‘Today
        is Wednesday. I leave on holiday in 19 days time. What day will that 
        be?”’ So the function must take a day name and a delta argument — the
        number of days to add — and should return the resulting day name:
    """

    def test_1_dayadd(self):
        self.assertEqual(day_add("Monday", 4), "Friday")

    def test_2_dayadd(self):
        self.assertEqual(day_add("Tuesday", 0), "Tuesday")

    def test_3_dayadd(self):
        self.assertEqual(day_add("Tuesday", 14), "Tuesday")

    def test_4_dayadd(self):
        self.assertEqual(day_add("Sunday", 100), "Tuesday")
    """
        Exercise 5: Can your day_add function already work with negative del-
        tas? For example, -1 would be yesterday, or -7 would be a week ago:
        If your function already works, explain why. If it does not work, ma-
        ke it work.
        Hint: Play with some cases of using the modulus function % (introduced
        at the beginning of the previous chapter). Specifically, explore what 
        happens to x % 7 when x is negative.
    """
    def test_1_negative_dayadd(self):
        self.assertEqual(day_add("Sunday", -1), "Saturday")

    def test_2_negative_dayadd(self):
        self.assertEqual(day_add("Sunday", -7), "Sunday")

    def test_2_negative_dayadd(self):
        self.assertEqual(day_add("Tuesday", -100), "Sunday")

    # The day_add function already works with negative values due to it being programmed
    # using modulus


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()



