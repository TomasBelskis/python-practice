"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 5 exercise 9
@Description: In the turtle bar chart program, what do you expect
              to happen if one or more of the data values in the list
              is negative? Try it out. Change the program so that when
              it prints the text value for the negative bars, it puts the
              text below the bottom of the bar.
"""

import turtle



def draw_bar(t, height):
    """ Get the turtle t to draw a bar of height"""
    t.begin_fill()
    t.left(90)
    t.forward(height) # Draw up the left side
    if (height < 0):
        t.penup()
        t.forward(-11)
        t.write(" " + str(height))
        t.forward(11)
        t.pendown()
    else:
        t.write(" " + str(height))

    t.right(90)
    t.forward(40) # Width of the bar, along the top
    t.right(90)
    t.forward(height) # Draw down the right side
    t.left(90) # Rotate to a starting postion
    t.end_fill()
    t.penup()
    t.forward(10) # Make some space between bars
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.speed(10)
t.color("lightgreen", "white")
t.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220, -210]


for v in xs:
    if (v < 100):
        t.fillcolor("green")
        draw_bar(t, v)
    elif (v >= 100 and v <= 200):
        t.fillcolor("yellow")
        draw_bar(t, v)
    elif (v > 200):
        t.fillcolor("red")
        draw_bar(t, v)
    else:
        draw_bar(t, v)



wn.mainloop()

