"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 2
@description: A program that draws increasing squares starting from small square to a large one. Assume the innermost
              square is 20 units per side, and each successive square
              is 20 units bigger, per side, than the one inside it.
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

def drawSquare(t, s):
    """
    :param t: turtle
    :param s: size
    :return: none
    """
    for i in range(4):
        t.forward(s)
        t.left(90)

def drawAreaSquares(n, size, distance): # Will refactor this from exercise 1 to draw squares increasing in size
    x = -30
    y = -10
    for i in range(n):
        t.pendown()
        drawSquare(t, size)
        t.penup()
        t.setposition(x,y)
        size += 20
        x -= 10
        y -= 10


w = makeWindow("black", "Chapter 4 exercise 1")
t = makeTurtle("green",5,(-20,0))

drawAreaSquares(10, 20, 20)

w.mainloop()