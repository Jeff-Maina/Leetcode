'''
1037. Valid Boomerang
Easy

Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 
'''

# collinearity of three points formula.


def isBoomerang(points):

    # check duplicates
    if points[0] == points[1] or points[1] == points[2] or points[2] == points[0]:
        return False

    x1, x2, x3 = points[0][0], points[1][0], points[2][0]
    y1, y2, y3 = points[0][1], points[1][1], points[2][1]

    # math formula -> x1(y2 – y3) + x2(y3 – y1) + x3(y1 – y2) = 0
    c = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)

    return c != 0


print(isBoomerang([[1,1],[2,3],[3,2]]))
