'''
Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
'''


def kLengthApart(nums, k):
    t = len(nums)

    # Find the index of the first 1 and use it as your starting point
    try:
        ind = nums.index(1)
    except ValueError:
        return True

    for i in range(ind+1, t):
        if nums[i] == 1:
            d = i - ind

            if d > k:
                ind = i
            else:
                return False

    return True


print(kLengthApart([ 0, 0, 0, 1, 0, 0,  ], 2))
