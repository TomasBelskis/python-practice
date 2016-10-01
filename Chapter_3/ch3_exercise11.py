# @author: Tomas Belskis
# EX 11: Write program to draw a shape (Shape is a star).

import turtle

wn = turtle.Screen()
star = turtle.Turtle()

star.hideturtle();

for i in range(5):
    star.forward(250)
    star.left(-144)

wn.mainloop()