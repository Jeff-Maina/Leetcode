'''
1304. Find N Unique Integers Sum up to Zero
Easy
Given an integer n, return any array containing n unique integers such that they add up to 0.
'''


def sumZero(n):

    ans = [0]*n

    for i in range(1,n):
        ans[i] = i

    ans[0] = -sum(ans)

    return ans


print(sumZero())
