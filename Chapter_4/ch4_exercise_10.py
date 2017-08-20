"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 10
@description: Extend your program above. Draw five stars, but between each, pick up the pen,
              move forward by 350 units, turn right by 144, put the pen down, and draw the next star.
              You’ll get something like this:
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

def draw_stars(t,n):
    for i in range(n):
        draw_star(t)
        t.penup()
        t.forward(350)
        t.right(144)
        t.pendown()

w = makeWindow("black", "Chapter 4 exercise 1")
t = makeTurtle("green",5,(-20,0))
draw_stars(t,5)


w.mainloop()