'''
2278. Percentage of Letter in String
Easy
Topics
Companies
Hint
Given a string s and a character letter, return the percentage of characters in s that equal letter rounded down to the nearest whole percent.

 
'''

import math


def percentageLetter(self, s: str, letter: str):
    l = len(s)
    c = s.count(letter)

    return math.floor((c/l)*100) if c else 0


