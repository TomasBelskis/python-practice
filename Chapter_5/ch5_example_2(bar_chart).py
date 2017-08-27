"""
Chapter 5 example 2, drawing a bar chart using turtle
module.
"""
import turtle



def draw_bar(t, height):
    """ Get the turtle t to draw a bar of height"""
    t.begin_fill()
    t.left(90)
    t.forward(height) # Draw up the left side
    t.write(" " + str(height))
    t.right(90)
    t.forward(40) # Width of the bar, along the top
    t.right(90)
    t.forward(height) # Draw down the right side
    t.left(90) # Rotate to a starting postion
    t.end_fill()
    t.forward(10) # Make some space between bars

wn = turtle.Screen()
wn.bgcolor("black")

t = turtle.Turtle()
t.color("lightgreen", "white")
t.pensize(3)

xs = [48, 117, 200, 240, 160, 260, 220]


for v in xs:
    draw_bar(t,v)

wn.mainloop()



