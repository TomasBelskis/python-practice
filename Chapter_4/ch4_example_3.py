# This example draws a rectangle and a square by caling rectangle function

import turtle

def draw_rectangle(t, w, h):
    """Get turle t to draw a rectangle of width w and height h."""
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

def draw_square(tx, sz): # A new version of a draw square
    draw_rectangle(tx, sz, sz)


wn = turtle.Screen()		# Set up the window and its attribute
wn.bgcolor("lightgreen")

tess = turtle.Turtle()		# Create tess and set some attributes
tess.pensize(3)

size = 50			# Size of the smallest square
width = 150
height = 60
draw_square(tess, size)
draw_rectangle(tess, width, height)

wn.mainloop()
