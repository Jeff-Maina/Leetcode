'''
674. Longest Continuous Increasing Subsequence
Easy
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].
'''


def findLengthOfLCIS(nums):
        array_length = len(nums)
      
        result = current_length = 1
      
        for i in range(1, array_length):
            
            if nums[i - 1] < nums[i]:
                current_length += 1
            else:
                current_length = 1
          
            result = max(result, current_length)
      
        return result


print(findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]))


print([1, 3, 5, 7][0:1])
