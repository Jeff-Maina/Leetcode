'''
35. Search Insert Position
Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''


def searchInsert(nums, target):


    left = 0
    right = len(nums) - 1


    while right >= left:
        # floor division
        mid = (left + right)//2

        if nums[mid] == target:
            return nums.index(target)
        elif target > nums[mid]:
            # shift left to a position over mid
            left = mid + 1
        elif target < nums[mid]:
            # shift left to a position behind mid
            right = mid - 1

    # otherwise return the left pointer (where it would be)
    return left


print(searchInsert([1, 3, 5, 6], 2))
