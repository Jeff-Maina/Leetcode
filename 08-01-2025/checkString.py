'''
2124. Check if All A's Appears Before All B's
Easy
Topics
Companies
Hint
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
'''


def checkString(s):
    c = s.count('a')

    if c == 0:
        return True

    for i in range(len(s)):
        if s[i] == 'b' and i < c:
            return False

    return True
