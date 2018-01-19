# -*- coding: utf-8 -*-
"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 8 exercise 2
@Description: Exercises 2,
              Modify:
              1 prefixes = "JKLMNOPQ"
              2 suffix = "ack"
              3
              4 for letter in prefixes:
              5 print(letter + suffix)
              so that Ouack and Quack are spelled correctly.
"""

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter + 'u' + suffix)
    else:
        print(letter + suffix)