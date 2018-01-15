# -*- coding: utf-8 -*-
"""
Description: 17. You and your friend are in a team to write
                 a two-player game, human against computer,
                 such as Tic-Tac-Toe / Noughts and Crosses.
                 Your friend will write the logic to play one
                 round of the game, while you will write the
                 logic to allow many rounds of play, keep score,
                 decide who plays, first, etc. The two of you
                 negotiate on how the two parts of the program will
                 fit together, and you come up with this simple
                 scaffolding (which your friend will improve later):

                 (a) Write the main program which repeatedly calls this function to
                 play the game, and after each round it announces the outcome as
                 “I win!”, “You win!”, or “Game drawn!”. It then asks the player
                 “Do you want to play again?” and either plays again, or says
                 “Goodbye”, and terminates.

                 (b) Keep score of how many wins each player has had, and how many draws
                 there have been. After each round of play, also announce the scores.

                 (c) Add logic so that the players take turns to play first.

                 (d) Compute the percentage of wins for the human, out of all games
                 played. Also announce this at the end of each round.

                 (e) Draw a flowchart of your logic.

"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 17
@Description: Exercises 17
"""
import random


# Your friend will complete this function
def play_once(human_plays_first):
    """
        Must play one round of the game. If the parameter
        is True, the human gets to play first, else the
        computer gets to play first. When the round ends,
        the return value of the function is one of
        -1 (human wins), 0 (game drawn), 1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment

    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1, 2)
    print("Human plays first={0}, winner={1} "
          .format(human_plays_first, result))
    return result


# Function to determine who goes first
def who_starts():
    print("Select a number from 1 to 10")
    inpt = int(input())

    rng = random.Random()
    result = rng.randrange(1,10)

    if inpt == result or ((inpt - 2) <= result and (inpt + 2) >= result):
        return True
    else:
        return False


# Function for continuous gameplay
def play_the_game():
    continue_game = True
    player_win = 0
    draw = 0
    computer_win = 0
    starting_player = who_starts()
    while continue_game:
        result = play_once(starting_player)
        if result == -1:
            print("I win!")
            player_win += 1
        elif result == 0:
            print("Game drawn!")
            draw += 1
        else:
            print("You win!")
            computer_win += 1

        print("Current score Player win: ", player_win," Draw: ", draw, " Computer win: ",
              computer_win, "\nDo want to continue, yes or no?")
        inpt = input()

        # Setting the players to rotate turns:
        if starting_player: starting_player = False
        else: starting_player = True

        if inpt == "no":
            print("Final scores Player win: ", player_win," Draw: ", draw, " Computer win: ",
              computer_win,"\nGoodbye!")
            continue_game = False
            break


play_the_game()
