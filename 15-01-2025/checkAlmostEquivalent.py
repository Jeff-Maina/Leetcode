'''
2068. Check Whether Two Strings are Almost Equivalent
Easy

Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.
'''

from collections import Counter

def checkAlmostEquivalent(word1, word2):
    freq1 = Counter(word1)
    freq2 = Counter(word2)

    # the trick is to iterate over all letters

    for letter in 'abcdefghijklmnopqrstuvwxyz':
        diff = abs(freq1.get(letter, 0) - freq2.get(letter, 0))
        if diff > 3:
            return False
        
    return True


print(checkAlmostEquivalent("aaaa", "bccb"))
