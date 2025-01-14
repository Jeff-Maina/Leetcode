'''
2733. Neither Minimum nor Maximum
Easy
Topics
Companies
Hint
Given an integer array nums containing distinct positive integers, find and return any number from the array that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.


'''


def findNonMinOrMax(nums):
    if len(nums) <= 2:
        return -1
    else:
        return sorted(nums[:3])[1]


print(findNonMinOrMax([3, 2, 1, 4]))

print([1, 2, 3, 4, 5, 5][3:])
