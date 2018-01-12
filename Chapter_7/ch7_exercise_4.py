# -*- coding: utf-8 -*-
"""
Description: 4. Count how many words in a list have length 5.

"""

"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 7 exercise 4
@Description: Exercises 4
"""

def count_words_lenght5(wl):
 count = 0
 for n in wl:
     if len(n) > 5:
         count += 1
 return count

list_of_words = ["hi","heroes","macaroon","joke","yes"]

print(count_words_lenght5(list_of_words))
