# -*- coding: utf-8 -*-
"""
Description: 11. Revisit the drunk pirate problem from the exercises
                 in chapter 3. This time, the drunk pirate makes a turn,
                 and then takes some steps forward, and repeats this. Our
                 social science student now records pairs of data: the
                 angle of each turn, and the number of steps taken after
                 the turn. Her experimental data is [(160, 20), (-43, 10),
                 (270, 8), (-43, 12)]. Use a turtle to draw the path taken
                 by our drunk friend.
"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 11
@Description: Exercises 11
"""

import turtle

wn = turtle.Screen()
drunk = turtle.Turtle()

exp_data = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for i, j in exp_data:
    drunk.left(i)
    drunk.forward(j)


wn.mainloop()
