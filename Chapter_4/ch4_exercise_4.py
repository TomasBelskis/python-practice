"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 4
@description: Drawing a pattern
"""

import turtle

def makeWindow(color, title, size):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    w.screensize(size,size)
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

def drawSquare(t, s):
    """
    :param t: turtle
    :param s: size
    :return: none
    """
    for i in range(4):
        t.forward(s)
        t.left(90)

def drawSquaresInRotation(n, size, distance): # Will refactor this from exercise 1 to draw squares increasing in size
    for i in range(n):
        drawSquare(t, size)
        t.left(10)


w = makeWindow("black", "Chapter 4 exercise 1",600)
t = makeTurtle("green",5,(0,0))

drawSquaresInRotation(40,250,20)

w.mainloop()