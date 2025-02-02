'''
1827. Minimum Operations to Make the Array Increasing
Easy

You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.
'''


def minOperations(nums):

    if len(nums) == 0:
        return 0

    count = 0

    for i in range(1, len(nums)):
        current = nums[i]
        prev = nums[i-1]


        if current <= prev:
            # add one to ensure it is higher than the current
            new = (prev - current) + 1
            count += new
            nums[i] = new

    return count


print(minOperations([8]))
