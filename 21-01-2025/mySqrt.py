'''

69. Sqrt(x)
Easy
Topics
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

'''


def mySqrt(x):

    if x == 1:
        return 1
    
    if x == 0:
        return 0

    left = 1
    right = int(x//2)

    print(left,right)

    while right >= left:
        mid = (right + left)//2
        sq = mid*mid

        print(f'the number at the mid is {mid} -> ({sq}), with left -> {left} and right -> {right}')

        if sq > x:
            right = mid - 1
        elif sq < x:
            left = mid + 1
        else:
            return mid,
        
    return right 


print(mySqrt(8))