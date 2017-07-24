"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 3
@description: Write a void function draw_poly(t, n, sz) which makes
              a turtle draw a regular polygon. When called with
              draw_poly(tess, 8, 50), it will draw a polygon shape:.
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

def draw_poly(tess, sides, lenght):
    for i in range(sides):
        tess.forward(lenght)
        tess.right(315)



w = makeWindow("black", "Chapter 4 exercise 1")
t = makeTurtle("green",5,(-20,0))

draw_poly(t,  8, 50)

w.mainloop()