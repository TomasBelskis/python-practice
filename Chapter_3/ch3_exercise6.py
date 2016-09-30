# @author: Tomas Belskis
# EX 6: Use for loops to make a turtle draw these regular
# polygons (regular means all sides the same lengths, all
# all angles the same):

# 1: An equilateral triangle (120 angle)
# 2: A square (90 angle)
# 3: A hexagon (six sides) (60 angle)
# 4: An octagon (eight sides) (135 angle)

import turtle

wn = turtle.Screen()

trex = turtle.Turtle()
trex.color("red")
squag = turtle.Turtle()
squag.color("blue")
hexar = turtle.Turtle()
hexar.color("green")
octopus = turtle.Turtle()
octopus.color("purple")

# An equilateral triangle (120 degree angle)
for i in range(3):
    trex.forward(30)
    trex.left(120)

# A square (90 degree angle)
for j in range(4):
    squag.forward(50)
    squag.left(90)

# A hexagon (60 degree angle)
for h in range(6):
    hexar.forward(70)
    hexar.left(60)

# An octagon (135 angle)
for o in range(8):
    octopus.forward(90)
    octopus.left(45)

wn.mainloop()