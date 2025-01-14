'''
1189. Maximum Number of Balloons
Easy

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''

import math


def maxNumberOfBalloons(text):

    h = {i: 'balloon'.count(i) for i in 'balloon'}

    ans = []

    for i in h:
        c = text.count(i)

        if c < h[i]:
            return 0
        else:
            d = (c/h[i])
            ans.append(d)

    return int(math.floor(min(ans)))


print(maxNumberOfBalloons("llo"))
