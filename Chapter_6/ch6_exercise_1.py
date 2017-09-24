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
import math

# Exercise 1
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

# Exercise 2
def day_name(num):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(len(days)):
        if i == num:
            return days[i]

    return "None"

# Exercise 3
def day_num(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    for i in range(len(days)):
        if days[i] == day:
            return i

    return "None"

# Exercise 4 & 5
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

# Exercise 6
def days_in_month(month):
    monthsDays = {'January':31, 'February':28, 'March':31, 'April':30,
                  'May':31, 'June':30, 'July':31, 'August':31, 'September':30,
                  'October':31, 'November':30, 'December':31}

    for k, v in monthsDays.items():
        if k == month:
            return v

    return "None"

# Exercise 7 & 8
def to_secs(h, m, s):
    return int((h * 3600) + (m * 60) + s)

# Exercise 9
def hours_in(s):
    return int(s/3600)

def minutes_in(s):
    return int((s%3600)/60)

def seconds_in(s):
    return int(s%60)

# Exercise 11
def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1

    return "None"

# Exercise 12
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# Exercise 13
def slope(x1, y1, x2, y2):
    return (y2 - y1)/(x2 - x1)

# Exercise 13 (Part 2)
def intercept(x1, y1, x2, y2):
    m = slope(x1, y1, x2, y2)
    return y1 - m * x1

# Exercise 14
def is_even(n):
    if (n % 2) == 0:
        return True
    else:
        return False

    return "None"

# Exercise 15
def is_odd(n):
    if (n % 2) != 0:
        return True
    else:
        return False

    return "None"

# Exercise 16
def is_factor(n1, n2):
    if (n1 > n2):
        if (n1 % n2) == 0:
            return True
        else:
            return False
    elif (n1 < n2):
        if(n2 % n1) == 0:
            return True
        else:
            return False

    return "None"

def is_multiple(n1, n2):
    return n1 % n2 == 0

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

    """
        Exercise 6: Write a function days_in_month which takes the name of a 
        month, and returns the number of days in the month. Ignore leap years:
    """
    def test_1_daysinmonth(self):
        self.assertEqual(days_in_month("February"), 28)

    def test_2_daysinmonth(self):
        self.assertEqual(days_in_month("December"), 31)

    """
        Exercise 7: Write a function to_secs that converts hours, minutes and
        seconds to a total number of seconds. Here are some tests that should pass:
    """
    def test_1_tosecs(self):
        self.assertEqual(to_secs(2, 30, 10), 9010)

    def test_2_tosecs(self):
        self.assertEqual(to_secs(2, 0, 0), 7200)

    def test_3_tosecs(self):
        self.assertEqual(to_secs(0, 2, 0), 120)

    def test_4_tosecs(self):
        self.assertEqual(to_secs(0, 0, 42), 42)

    def test_5_tosecs(self):
        self.assertEqual(to_secs(0, -10, 10), -590)

    """
        Exercise 8: Extend to_secs so that it can cope with real values as 
        inputs. It should always return an integer number of seconds (truncated 
        towards zero):
    """
    def test_1_tosecs_real(self):
        self.assertEqual(to_secs(2.5, 0, 10.71), 9010)

    def test_2_tosecs_real(self):
        self.assertEqual(to_secs(2.433, 0, 0), 8758)

    """
        Exercises 9: Write three functions that are the “inverses” of to_secs:  
                        (a) hours_in returns the whole integer number of hours represented by a total num-
                        ber of seconds.
                        (b) minutes_in returns the whole integer number of left over minutes in a total number
                        of seconds, once the hours have been taken out.
                        (c) seconds_in returns the left over seconds represented by a total number of sec-
                        onds.
                        You may assume that the total number of seconds passed to these functions is an 
                        integer. Here are some test cases:
    """
    def test_1_hoursin(self):
        self.assertEqual(hours_in(9010), 2)

    def test_1_minutesin(self):
        self.assertEqual(minutes_in(9010), 30)

    def test_1_secondsin(self):
        self.assertEqual(seconds_in(9010), 10)

    """
        Exercise 10: Which of these tests fail? Explain why.
    """
    # def test_1_ex9(self):
        # self.assertEqual(3 % 4, 0) # Mod returns 3, because 4 doesn't go into 3

    def test_2_ex9(self):
        self.assertEqual(3 % 4, 3)

    #def test_3_ex9(self):
       # self.assertEqual(3 / 4, 0) # Returns a real value of 0.75

    def test_4_ex9(self):
        self.assertEqual(3 // 4, 0)

    # def test_5_ex9(self):
       #  self.assertEqual(3 + 4 * 2, 14) # Multiplication is executed first

   # def test_6_ex9(self):
       # self.assertEqual(4 - 2 + 2, 0) # Arithmetic operations executed left to right

    def test_7_ex9(self):
        self.assertEqual(len("hello, world!"), 13)

    """
        Exercise 11: Write a compare function that returns 1 if a > b, 0 if 
        a == b, and -1 if a < b
    """
    def test_1_compare(self):
        self.assertEqual(compare(5, 4), 1)

    def test_2_compare(self):
        self.assertEqual(compare(7, 7), 0)

    def test_3_compare(self):
        self.assertEqual(compare(2, 3), -1)

    def test_4_compare(self):
        self.assertEqual(compare(42, 1), 1)

    """
        Exercise 12: Write a function called hypotenuse that returns the length 
        of the hypotenuse of a right triangle given the lengths of the two legs 
        as parameters:
    """
    def test_1_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5.0)

    def test_2_hypotenuse(self):
        self.assertEqual(hypotenuse(12, 5), 13.0)

    def test_3_hypotenuse(self):
        self.assertEqual(hypotenuse(24, 7), 25.0)

    def test_4_hypotenuse(self):
        self.assertEqual(hypotenuse(9, 12), 15.0)

    """
        Exercise 13: Write a function slope(x1, y1, x2, y2) that returns the
        slope of the line through the points (x1, y1) and (x2, y2). Be sure 
        your implementation of slope can pass the following tests:
    """
    def test_1_slope(self):
        self.assertEqual(slope(5, 3, 4, 2), 1.0)

    def test_2_slope(self):
        self.assertEqual(slope(1, 2, 3, 2), 0.0)

    def test_3_slope(selfs):
        selfs.assertEqual(slope(1, 2, 3, 3), 0.5)

    def test_4_slope(self):
        self.assertEqual(slope(2, 4, 1, 2), 2.0)
    """
        Exercise 13 (Part 2): Then use a call to slope in a new function nam-
        ed intercept (x1, y1, x2, y2) that returns the y-intercept of the li-
        ne through the points (x1, y1) and (x2, y2)

    """
    def test_1_intercept(self):
        self.assertEqual(intercept(1, 6, 3, 12), 3.0)

    def test_2_intercept(self):
        self.assertEqual(intercept(6, 1, 1, 6), 7.0)

    def test_3_intercept(self):
        self.assertEqual(intercept(4, 6, 12, 8), 5.0)

    """
        Exercise 14: Write a function called is_even(n) that takes an integer 
        as an argument and returns True if the argument is an even number and
        False if it is odd.
        Add your own tests to the test suite.
    """
    def test_1_iseven(self):
        self.assertTrue(is_even(4))

    def test_2_iseven(self):
        self.assertTrue(is_even(12))

    def test_3_iseven(self):
        self.assertFalse(is_even(19))
    """
        Exercise 15: Now write the function is_odd(n) that returns True when n 
        is odd and False oth- erwise. Include unit tests for this function too.
        Finally, modify it so that it uses a call to is_even to determine if its 
        argument is an odd integer, and ensure that its test still pass.
    """
    def test_1_isodd(self):
        self.assertTrue(is_odd(3))

    def test_2_isodd(self):
        self.assertTrue(is_odd(15))

    def test_3_isodd(self):
        self.assertFalse(is_odd(6))

    def test_4_isodd(self):
        self.assertFalse(is_even(17))

    """
        Exercise 16: Write a function is_factor(f, n) that passes these tests:
    """
    def test_1_isfactor(self):
        self.assertTrue(is_factor(3, 12))

    def test_2_isfactor(self):
        self.assertFalse(is_factor(5, 12))

    def test_3_isfactor(self):
        self.assertTrue(is_factor(7, 14))

    def test_4_isfactor(self):
        self.assertFalse(is_factor(7, 15))

    def test_5_isfactor(self):
        self.assertTrue(is_factor(1, 15))

    def test_6_isfactor(self):
        self.assertTrue(is_factor(15, 15))

    """
        Exercise 17: Write is_multiple to satisfy these unit tests
    """
    def test_1_ismultiple(self):
        self.assertTrue(is_multiple(12, 3))

    def test_2_ismultiple(self):
        self.assertTrue(is_multiple(12, 4))

    def test_3_ismultiple(self):
        self.assertFalse(is_multiple(12, 5))

    def test_4_ismultiple(self):
        self.assertTrue(is_multiple(12, 6))

    def test_5_ismultiple(self):
        self.assertFalse(is_multiple(12, 7))

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()



