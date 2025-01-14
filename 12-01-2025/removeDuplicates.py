'''
1047. Remove All Adjacent Duplicates In String
Easy

You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.
'''


def removeDuplicates(s):
    cs = ''

    for i in range(len(s)):
        if len(cs) < 1:
            cs += s[i]
        else:
            if s[i] == cs[-1]:
                cs = cs[:-1]
                continue
            else:
                cs += s[i]

    return cs


print(removeDuplicates("azxxzy"))


# 0ms - using a stack

# similar implementation to my answer only that it is using a list and not a string


def removeDuplicates2(s):
    stack = []

    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    return ''.join(stack)
