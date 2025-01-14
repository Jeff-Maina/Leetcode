arr = [8, 1, 2, 2, 3]


# this has a complexity of O(N*N)
def smallerNumbersThanCurrent(nums):
    res = []
    for num in nums:
        counter = 0

        for i in range(len(nums)):
            if nums[i] < num:
                counter += 1

        res.append(counter)

    return res


print(smallerNumbersThanCurrent(arr))

# this has a complexity of O(N)


def smallerNumbersThanCurrent2(nums):
    temp = sorted(nums)

    d = {}

    for (index, num) in enumerate(temp):
        if num not in d:
            d[num] = index

    res = [d[i] for i in nums]

    return res


print(smallerNumbersThanCurrent2(arr))


def smallerNumbersThanCurrent3(nums):
    count = [0]*102

    for num in nums:
        count[num+1] += 1

    for i in range(1, 102):
        count[i] += count[i-1]

    return [count[num] for num in nums]


print(smallerNumbersThanCurrent3(arr))
