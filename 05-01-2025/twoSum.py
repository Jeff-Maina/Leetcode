arr = [3, 3]


def twoSum(nums, target):
    l = {}

    for (index, num) in enumerate(nums):
        check = target - num

        if check in l:
            return [l[check], index]

        l[num] = index


print(twoSum(arr, 6))


# the trick here is to store the result in a dictionary with the values as the keys to make it easier to get the inde later on