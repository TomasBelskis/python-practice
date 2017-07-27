"""
@author: Tomas Belskis
@exercise: Chapter 4 Exercise 6
@description: Rewrite a void function draw_equitriangle(t, sz) which calls
                draw_poly from the previous question to have its turtle draw a equilateral triangle.
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
        tess.left(120)

def draw_equitriangle(tess, sz):
    draw_poly(tess, 3, sz)

w = makeWindow("black", "Chapter 4 exercise 1")
t = makeTurtle("green",5,(-20,0))

draw_equitriangle(t,200)

w.mainloop()