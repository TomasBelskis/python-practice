#@author Tomas Belskis
#Extending turle program

# 1.Modify this turle2 so that before it creates the window, it prompts
#the user to enter he desired background color. It should store the
#user's responses in variable, and modify the color of the window
#according to user's wishes.

# 2.Do similar changes to allow the user, at runtime, to set tess color.

# 3.Do the same for the width of tess pen. Hint: your dialog with the
#will return a string, but tess pensize method expects its argument to
#be an int. So you'll need to convert the string to an int before you pass
#it to pensize.

import turtle


canvasBgColor = input("Enter the name of a color for a choice of a background color! ")

wn = turtle.Screen()
wn.bgcolor(canvasBgColor)
tess = turtle.Turtle()

tessColor = input("Enter tess color! ")
tess.color(tessColor)

tessPensize = input("Enter tess pensize! ")
tess.pensize(tessPensize)

tess.forward(150)
tess.left(130)
tess.forward(250)

wn.mainloop()