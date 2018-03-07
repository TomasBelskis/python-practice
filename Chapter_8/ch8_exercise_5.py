# -*- coding: utf-8 -*-
"""
@Author: Tomas Belskis
@Licence: MIT
@Exercise: Chapter 8
@Description: Exercise 5: Assign to a variable in your program a triple-quoted
                          string that contains your favourite paragraph of text
                          — perhaps a poem, a speech, instructions to bake a cake,
                          some inspirational verses, etc.
                          Write a function which removes all punctuation from the string,
                          breaks the string into a list of words, and counts the number
                          of words in your text that contain the letter “e”.
                          Your program should print an analysis of the text like this:
                          Your text contains 243 words, of which 109 (44.8%) contain an "e".

"""
import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

def find(strng, ch, start=0, end=None):
    ix = start
    if end is None:
        end = len(strng)
    while ix < end:
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

def calculate_percentage(val1, val2):
    return round((val1 / val2) * 100, 2)

def print_stats(string):
    wds = remove_punctuation(string).split()
    word_count = len(wds)
    e_count = 0
    for w in wds:
        if find(w, "e") != -1:
            e_count += 1

    return "Your text contains {0} words, of which {1} ({2}%) contain an \"e\".".format(word_count, e_count, calculate_percentage(e_count, word_count))


paragraph = """ Two roads diverged in a yellow wood,
                And sorry I could not travel both
                And be one traveler, long I stood
                And looked down one as far as I could
                To where it bent in the undergrowth;
                
                Then took the other, as just as fair,
                And having perhaps the better claim,
                Because it was grassy and wanted wear;
                Though as for that the passing there
                Had worn them really about the same,
                
                And both that morning equally lay
                In leaves no step had trodden black.
                Oh, I kept the first for another day!
                Yet knowing how way leads on to way,
                I doubted if I should ever come back.
                
                I shall be telling this with a sigh
                Somewhere ages and ages hence:
                Two roads diverged in a wood, and I—
                I took the one less traveled by,
                And that has made all the difference."""

print(print_stats(paragraph))