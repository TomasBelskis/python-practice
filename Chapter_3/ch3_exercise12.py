# @author: Tomas Belskis
# EX 12: Write a program to draw a face of a clock that look.

import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.shape("turtle")
tess.color("blue")
tess.stamp()
angle = 0

for i in range(12):
    tess.penup()
    tess.forward(100)
    tess.pendown()
    tess.pensize(4)
    tess.forward(10)
    tess.penup()
    tess.forward(20)
    tess.pendown()
    tess.stamp()
    tess.penup()
    tess.forward(-130)
    tess.left(angle+30)

wn.mainloop()