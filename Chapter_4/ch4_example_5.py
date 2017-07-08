"""
Example 5,  refactoring simple turtle program using functions:
"""
import turtle

def make_window(color, title):
    """
    Set up the window with the given background color and title.
    :param color:
    :param title:
    :return: window
    """
    w=turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, size):
    """
    Set up a turtle with given color and pensize.
    :param color:
    :param size:
    :return: turtle
    """
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    return t

wn = make_window("lightgreen","Tess and Alex dancing")
tess = make_turtle("hotpink", 5)
alex = make_turtle("black", 1)
dave = make_turtle("yellow", 2)

ex=input("Type enter to exit")

