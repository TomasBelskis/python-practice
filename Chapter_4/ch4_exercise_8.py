"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 8
@description: Write a function area_of_circle(r) which returns the area of a circle of radius r.
"""

def area_of_circle(r):
    a = 3.14 * (r*r)
    return a

print("Area of circle of radius 5 is: ", area_of_circle(5))

exit=input("Press enter to exit!")