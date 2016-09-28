import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

# Assign list to variable
clrs = ["yellow", "red", "purple", "blue"]

for c in clrs:
    alex.color(c)
    alex.forward(70)
    alex.left(90)

wn.mainloop()

