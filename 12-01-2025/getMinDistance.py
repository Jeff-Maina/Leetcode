'''
1848. Minimum Distance to the Target Element
Easy
Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.
'''


def getMinDistance(nums, target, start):

    if nums[start] == target:
        return 0

    diff = [abs(start - i) for i, x in enumerate(nums) if x == target]


    return min(diff)


print(getMinDistance([1,1,1,1,1,1,1,1,1,1], 1, 9))
