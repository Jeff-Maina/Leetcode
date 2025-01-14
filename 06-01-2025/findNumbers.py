'''
- Given an array nums of integers, return how many of them contain an even number of digits.
'''
import math

'''

1
10 = tens
100
1,000 = thousands
10,000
100,000 = hundred thousands
1,000,000
10,000,000 = tens of millions
100,000,000

'''


nums = [555,901,482,1771]

'''
- converting integers to strings for each value in the list increases run time

'''

def findNumbers(nums):
    return len([i for i in nums if len(str(i)) % 2 == 0])

def findNumbers2(nums):
    return len([("%i" % i) for i in nums if len("%i" % i) % 2 == 0])


print(findNumbers(nums))
