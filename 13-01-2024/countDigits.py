'''
2520. Count the Digits That Divide a Number
Easy

Given an integer num, return the number of digits in num that divide num.

An integer val divides nums if nums % val == 0.

 
'''


def countDigits(num: int) -> int:
    return len([int(i) for i in str(num) if num % int(i) == 0])




print(countDigits(1248))
