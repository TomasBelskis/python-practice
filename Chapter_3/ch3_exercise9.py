# @author: Tomas Belskis
# EX 9: If you were going to draw a regular polygon with 18
# sides, what angle would you need to turn the turtle at
# each corner? ANSWER: 20

import turtle

wn = turtle.Screen()
wn.bgcolor("blue")
pol = turtle.Turtle()
pol.color("white")

for i in range(18):
    pol.forward(30)
    pol.left(20)

wn.mainloop()