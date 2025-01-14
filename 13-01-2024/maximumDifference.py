'''
2016. Maximum Difference Between Increasing Elements
Easy

Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
'''


def maximumDifference(nums):
    l = len(nums)

    j = 0
    minNum = nums[0]
    maxDiff = 0

    while j < l:
        diff = nums[j] - minNum

        maxDiff = max(maxDiff, diff)
        minNum = min(minNum, nums[j])

        j += 1

    return maxDiff if maxDiff else -1


print(maximumDifference([9,4,3,2]))
