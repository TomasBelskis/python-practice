# Chapter 4 examples page 39

import turtle 

# def Example function(p1, p2):
#	Statement

def draw_square(t, sz):
	"Make turtle t draw a square of sz."""	

	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()	# Sets up a window and its attributes
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")	
alex = turtle.Turtle()	# Create Alex 
draw_square(alex, 50)	# Call the function to draw the square
wn.mainloop()

