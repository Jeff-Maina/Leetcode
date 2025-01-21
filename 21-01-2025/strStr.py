'''
28. Find the Index of the First Occurrence in a String
Easy

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''


def strStr(haystack, needle):

    if len(haystack) < len(needle):
        return -1

    right = 0

    l2 = len(needle)

    while right < len(haystack):
        if haystack[right] == needle[0]:
            if haystack[right:right + l2] == needle:
                return right
            
        right += 1


    return -1


print(strStr("adbutsad", 'sad'))
