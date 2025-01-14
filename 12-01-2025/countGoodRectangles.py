'''
1725. Number Of Rectangles That Can Form The Largest Square
Easy

You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.

You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example, if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.

Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.

Return the number of rectangles that can make a square with a side length of maxLen.
'''


def countGoodRectangles(rectangles):

    maxLens = [min(i) for i in rectangles]

    count = maxLens.count(max(maxLens))

    return count


print(countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
