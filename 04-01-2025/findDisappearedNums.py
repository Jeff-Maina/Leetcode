def findDisappearedNumbers(nums):
    result = []
    num_set = set(nums)  # Set is created once
    l = len(nums)

    for i in range(1, l + 1):
        if i not in num_set:  # Membership check is efficient (O(1))
            result.append(i)

    return result

# avoid creating sets instide loops