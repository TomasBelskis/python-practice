"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 5 exercise 1
@Description: Assume the days of the week are numbered 0,1,2,3,4,5,6 from Sunday
              to Saturday. Write a function which is given the day number, and it
              returns the day name (a string).
"""

def day_of_the_week(d):
    if d == 0:
        return "Monday"
    elif d == 1:
        return "Tuesday"
    elif d == 2:
        return "Wednesday"
    elif d == 3:
        return "Thursday"
    elif d == 4:
        return "Friday"
    elif d == 5:
        return "Saturday"
    elif d == 6:
        return "Sunday"
    else:
        return "Invalid number, day doesn't exist"

print(day_of_the_week(4))
