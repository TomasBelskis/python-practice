# @author: Tomas Belskis
# EX 7: A drunk pirate makes a random turn and then takes 100 steps forward,
# makes another random turn, takes another 100 steps, turns another random
# amount, etc. A social science student records the angle of each turn
# before the next 100 steps are taken. Her experimental data is [160, -43,
# 270, -97, -43, 200, -940, 17, -86]. (Positive angles are counter-clockwise.)
# Use a turtle to draw the path taken by our drunk friend.
# EX 8: Enhance your program above to also tell us what the drunk pirate's
# heading is after he has finished stumbling around. (Assuming he begins at
# heading 0).

import turtle

wn = turtle.Screen()
drunk = turtle.Turtle()

exp_data = [160, -43, 270, -97, -43, 200, -940, 17, -86]

for i in exp_data:
    drunk.left(i)
    drunk.forward(100)

# Part of exercise 8 to determine pirates heading
print("Heading of a drunk pirate: ", drunk.heading())
wn.mainloop()

