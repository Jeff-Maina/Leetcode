'''
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
'''


def isValid(s):
    if len(s) % 2 != 0:
        return False

    stack = []
    pairs = ['()', '{}', '[]']

    for c in s:
        if c in '({[':
            stack.append(c)
        elif not stack or stack.pop() + c not in pairs:
            return False
        
    return not stack


print(isValid('()[]{}'))
