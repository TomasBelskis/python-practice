"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 9
@description: Write a void function to draw a star, where the length of each side
              is 100 units. (Hint:You should turn the turtle by 144 degrees at each point.)
"""

import turtle

def makeWindow(color, title):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    return w

def makeTurtle(color, size, pos):
    t = turtle.Turtle()
    t.speed(0)
    t.color(color)
    t.pensize(size)
    t.penup()
    t.setpos(pos)
    t.pendown()
    return t


def draw_star(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

w = makeWindow("black", "Chapter 4 exercise 1")
t = makeTurtle("green",5,(-20,0))

draw_star(t)

w.mainloop()