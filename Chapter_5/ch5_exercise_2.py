"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 5 exercise 2
@Description: You go on a wonderful holiday (perhaps to jail,
              if you don’t like happy exercises) leaving on day number 3 (a Wednesday).
              You return home after 137 sleeps. Write a general version of the program
              which asks for the starting day number, and the length of your stay, and it
              will tell you the name of day of the week you will return on.
"""

def day_of_the_week(s,e):
    days = ["Monday","Tuesday","Wendnesday","Thursday","Friday","Saturday","Sunday"]
    return_day = 0
    s -= 1
    return_day = s + (e % 7)

    if(return_day < 7 ):
        return days[return_day]
    else:
        return_day = return_day % 7
        return days[return_day]

print(day_of_the_week(6,11))