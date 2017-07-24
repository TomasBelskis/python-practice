"""
@author: Tomas Belskis
@exercise: Chapter 4 exercise 1
@description: Write a void (non-fruitful) function to draw a square.
              Use it in a program to draw the image shown below.
              Assume each side is 20 units.
              (Hint: notice that the turtle has already moved away from
              the ending point of the last square when the program ends.)
"""

import turtle

def make_window(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def make_turtle(color, size, pos):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.pensize(size)
    t.penup()
    t.setpos(pos)
    t.pendown()
    return t

def draw_square(t, s):
    """
    :param t: turtle
    :param s: size
    :return: none
    """
    for i in range(4):
        t.forward(s)
        t.left(90)

def draw_number_of_squares(n, size, distance):

 for i in range(n):
    draw_square(t, size)
    t.penup()
    t.forward(distance+size)
    t.pendown()


w = make_window("black", "Chapter 4 exercise 1")
t = make_turtle("green",5,(-200,0))

draw_number_of_squares(10, 20, 20)

w.mainloop()