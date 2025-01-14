def minTimeToVisitAllPoints(points):
    t = 0
    x1, y1 = points.pop()

    while points:

        x2, y2 = points.pop()

        t += max(abs(y2-y1), abs(x2-x1))

        x1, y1 = x2, y2

    return t

print(minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))