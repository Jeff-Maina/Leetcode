'''
859. Buddy Strings

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
'''

# solutions -> https://algo.monster/liteproblems/859

from collections import Counter


def buddyStrings(s, goal):
    len_s, len_g = len(s), len(goal)

    if len_s != len_g:
        return False

    counter_a, counter_b = Counter(s), Counter(goal)

    if counter_a != counter_b:
        return False

    # check how many times they differ
    diff = sum(1 for i in range(len_s) if s[i] != goal[i])

    # Return True if there are exactly two differences
    # (which can be swapped to make the strings equal)
    # Or if there's no difference and there are duplicate characters in the string
    # (which can be swapped with each other while keeping the string the same)
    return diff == 2 or (diff == 0 and any(value > 1 for value in counter_a.values()))


print(buddyStrings('ab', 'ba'))
'''

Notes

- Steps

    - Length check -> if s and goal have different lengths then its auto False
    - Char frequency -> Character frequency check, if they dont match == false
    - Check differing characters if 2 then True
    - Check for duplcate values - they can be switched without changing the string


'''


# 0ms

def buddyString2(s, goal):
    if len(s) != len(goal):
        return False

    # checks for duplicates
    if s == goal:
        for char in s:
            if s.count(char) > 1:
                return True
        return False

    difference = []

    for i in range(len(s)):
        if s[i] != goal[i]:
            difference.append((s[i], goal[i]))

    return len(difference) == 2 and difference[0] == difference[1][::-1]
