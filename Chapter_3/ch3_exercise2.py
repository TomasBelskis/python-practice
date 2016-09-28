# @author Tomas Belskis
# EX 2: Give three attributes of your cellphone object. Give three methods
# of your cellphone.

import turtle

wn  = turtle.Screen()
cellphone = turtle.Turtle()
cellphone.color("red")      #attribute = red, method=color
cellphone.shape("turtle")   #attribute = turtle, method=shape
cellphone.forward(30)       #attribute = 30, method=forward

wn.mainloop()