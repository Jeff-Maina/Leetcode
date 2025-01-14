
# Initial submission
def missingNumber(nums):
    nums.sort()

    for i in range(len(nums)):
        if not (i+1) in nums:
            return (i+1)

# efficient answer


def missingNumber2(nums):
    # we add 1 to include the last digit
    # summing is O(n)
    return sum(range(len(nums)+1)) - sum(nums)


print(missingNumber2([0, 1]))


# sorting in python is NlogN
