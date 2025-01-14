def thirdMax(nums):
    l = sorted(set(nums), reverse=True)

    if len(l) < 3:
        return max(nums)

    return l[2]


print(thirdMax([1, 1, 2]))


'''
In Python, the sorted() function takes an iterable (like a list, tuple, or string) and returns a new list with the elements sorted in ascending order, without modifying the original iterable
'''
