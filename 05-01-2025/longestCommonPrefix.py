def longestCommonPrefix(strs):

    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                return strs[j][:i]
    return strs[0]


def longestCommonPrefix2(strs):

    res = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        res += strs[0][i]

    return res


def longestCommonPrefix3(strs):
    chars = zip(*strs)
    res = ""

    for c in chars:
        if len(set(c)) == 1:
            res += c[0]
        else:
            break
    return res


print(longestCommonPrefix3(["flower", "flow", "floight"]))

'''
zip()  function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

eg zip(["flower", "flow", "floight"])

returns
('f', 'f', 'f') -> first values are paired together etc
('l', 'l', 'i')
('o', 'o', 'g')
('w', 'w', 'h')

- we then find lenght of each tuple converted to a set
- of value is one then all the letters in that position are similar and we therefore add it to the result
- if not we break out of the loop

'''
