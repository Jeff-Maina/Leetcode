'''
2605. Form Smallest Number From Two Digit Arrays
Solved
Easy

Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.

'''

def minNumber(nums1, nums2) -> int:
    h = {c: i for i, c in enumerate(nums1)}
    mins = sorted(set([min(nums1), min(nums2)]))

    d = []

    for n in nums2:
        if n in h:
            d.append(n)

    if len(d) >= 1:
        return min(d)
    else:
        return int(str(mins[0]) + str(mins[1]))

print(minNumber([4,1,3], [5,7]))
