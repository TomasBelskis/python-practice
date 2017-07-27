"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 5
@description: Drawing a spiral pattern square & angled.
"""

import turtle

def makeWindow(color, title, size):
    w = turtle.Screen()
    w.bgcolor(color)
    w.title(title)
    w.screensize()
    w.setup(width=1.0,height=1.0)
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

def drawSquare(t,s,r,s_size):
    """
    :param t: turtle
    :param s: size
    :return: none
    """
    for i in range(s_size):
        t.forward(s)
        t.right(r)
        s += 5

def drawSquaresInRotation(n,size,rotation,s_size): # Will refactor this from exercise 1 to draw squares increasing in size
    for i in range(n):
        drawSquare(t, size, rotation, s_size)


w = makeWindow("black", "Chapter 4 exercise 1",600)
t = makeTurtle("green",5,(0,0))

drawSquaresInRotation(1,10,90,120) # Set rotation 90 to make the spiral into a square, set it to 92 to rotate it slightly

w.mainloop()