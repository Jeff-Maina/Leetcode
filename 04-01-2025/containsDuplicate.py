from collections import Counter


arr = [1, 2, 3, 5, 8, 19, 28, 1, 2, 3]


# method 1
def containsDuplicate(nums):

    list = [nums.count(num) for num in nums]

    if max(list) >= 2:
        return True
    else:
        return False


# method 2 - most efficient
def containsDuplicate2(nums):
    return len(set(nums)) != len(nums)


# method 3 - using a counter function

def containsDuplicate(self, nums) -> bool:
    freq = Counter(nums)
    
    for num, freq in freq.items():
        if freq > 1:
            return True
    return False


print(containsDuplicate2(arr))



'''

- sets don't have duplicates and are therefore efficent data structures
- we use my_set.add(element) to add an element to the set
- we use my_set.remove(element) to remove an element from the set
- we use (element in set) to check if elements exists in the set
- we use set.discard(2) to remove and return an element


- other approaches - sort the numbers and check if two consecutive numbers are the same
- using a Counter function

'''
