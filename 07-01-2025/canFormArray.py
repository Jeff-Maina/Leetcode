'''
You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.
'''


def canFormArray(arr, pieces):

    d = {}

    res = []

    for i in range(len(pieces)):
        d[pieces[i][0]] = pieces[i]

    for v in arr:
        if v in d:
            res.extend(d[v])
        else:
            print(v)
            

    return res == arr


print(canFormArray([49,18,16],[[16,18,49]]))
