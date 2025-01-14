'''
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

'''


def subtractProductAndSum(n):

    arr = [int(i) for i in str(n)]

    s = sum(arr)

    product = arr[0]

    for n in range(1, len(arr)):
        product *= arr[n]


    return product - s


subtractProductAndSum(234)
