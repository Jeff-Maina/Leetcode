'''
2903. Find Indices With Index and Value Difference I
Easy

You are given a 0-indexed integer array nums having length n, an integer indexDifference, and an integer valueDifference.

Your task is to find two indices i and j, both in the range [0, n - 1], that satisfy the following conditions:

abs(i - j) >= indexDifference, and
abs(nums[i] - nums[j]) >= valueDifference
Return an integer array answer, where answer = [i, j] if there are two such indices, and answer = [-1, -1] otherwise. If there are multiple choices for the two indices, return any of them.

Note: i and j may be equal.
'''


def findIndices(nums, indexDifference: int, valueDifference: int):

    for i in range(len(nums)):
        for j in range(len(nums)):
            vd = abs(nums[j] - nums[i])
            id = abs(j - i)

            if vd >= valueDifference and id >= indexDifference:
                return [i, j]

    return [-1, -1]


print(findIndices([2, 1], 0, 0))
