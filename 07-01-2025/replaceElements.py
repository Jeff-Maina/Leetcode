def replaceElements(arr):
    if len(arr) == 1:
        return [-1]
     
    mv = min(arr)

    res = []

    for i in range(1,len(arr)):
        if arr[-i] > mv:
            res.append(arr[-i])
            mv = arr[-i]
        else:
            res.append(mv)
    
    res.reverse()
    res.append(-1)

    return res 


arr = [17, 18, 5, 4, 6, 1]


print(replaceElements(arr))

# time limit exceeded
def replaceElements2(self, arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """

    res = [max(arr[i+1:]) for i in range(0, len(arr)-1)]

    res.append(-1)

    return res
