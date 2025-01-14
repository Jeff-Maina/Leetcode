'''
2540. Minimum Common Value

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

'''

# using a hashset is not optimal = 17ms
def getCommon(nums1, nums2):
    h = {}

    for n in nums1:
        h[n] = n

    for n in nums2:
        if n in nums1:
            return n

    return -1

# 2 pointer approach: = 0ms
def getCommon2(nums1, nums2):

    i = j = 0

    l1, l2 = len(nums1), len(nums2)

    e1 = nums1[l1-1]
    s2 = nums2[0]

    if l1 < 1 or l2 < 1:
        return -1

    if s2 > e1:
        return -1

    while i < l1 and j < l2:
        if nums1[i] == nums2[j]:
            return nums1[i]

        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return -1


print(getCommon2([1, 2, 3], [2, 4]))
