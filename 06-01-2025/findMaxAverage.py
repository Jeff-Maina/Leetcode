
'''
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
'''


def findMaxAverage(nums, k):
    l = len(nums)

    current_sum = sum(nums[:k])

    max_sum = current_sum
  
    '''
    - Use float to maintain precision

    - use range(l-k) to find out how many more possible windows are there having removed the first
    - we then go ahead and find the sum by moving the left and right pointers hence
      we remove the first element of the prev window and add the last of the current window;

    '''
    for i in range(l-k):
        current_sum = current_sum - nums[i] + nums[k + i]

        if current_sum > max_sum:
            max_sum = current_sum

    return float(max_sum)/k


print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))
