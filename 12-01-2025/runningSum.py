def runningSum(nums):

    counter = 0

    ans = []

    for i in range(len(nums)):
        ans.append(counter + nums[i])
        counter += nums[i]

    return ans


print(runningSum([3,1,2,10,1]))
