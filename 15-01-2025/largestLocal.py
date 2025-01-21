'''
2373. Largest Local Values in a Matrix
Easy

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.
'''


def largestLocal(grid):

    n = len(grid[0])
    m = len(grid)

    ans = []

    for i in range(m-2):  # upto m-3 rows
        for j in range(n-2):  # upto n-3 columns
            # this checks every 3*3 window by slicing three rows upto 3cols everytime
            window = [row[j:j+3] for row in grid[i:i+3]]

            m = max(max(row) for row in window)

            ans.append(m)

    res = []

    for h in range(0, len(ans), n-2):
        res.append(ans[h:h+(n-2)])

    return res


print(largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))
