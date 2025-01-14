'''
2570. Merge Two 2D Arrays by Summing Values
Easy
Topics
Companies
Hint
You are given two 2D integer arrays nums1 and nums2.

nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
Each array contains unique ids and is sorted in ascending order by id.

Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

Only ids that appear in at least one of the two arrays should be included in the resulting array.
Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays then its value in that array is considered to be 0.
Return the resulting array. The returned array must be sorted in ascending order by id.
'''

# 0ms
def mergeArrays(nums1, nums2):
    h = {}

    for i in nums1:
        h[i[0]] = i[1]

    for n in nums2:
        if n[0] in h:
            h[n[0]] += n[1]
        else:
            h[n[0]] = n[1]

    res = []

    for i in h:
        res.append([i, h[i]])

    res.sort()

    return res


print(mergeArrays([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))

# 2 pointe method


def mergeArrays2(nums1, nums2):
    i = j = 0

    l1, l2 = len(nums1), len(nums2)

    h = {}

    while i < l1 and j < l2:
        if nums1[i][0] == nums2[j][0]:
            h[nums1[i][0]] = nums1[i][1] + nums2[j][1]

            i += 1
            j += 1
        elif nums1[i][0] < nums2[j][0]:
            h[nums1[i][0]] = nums1[i][1]
            i += 1
        else:
            h[nums2[j][0]] = nums2[j][1]
            j += 1

    return sorted([[i, x] for (i, x) in h.items()])


print(mergeArrays2([[1, 2], [2, 3], [4, 5]], [[1, 4], [3, 2], [4, 1]]))
