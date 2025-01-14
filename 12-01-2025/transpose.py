'''
867. Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

'''

def transpose(matrix):

    vals = zip(*matrix)

    ans = []

    for val in vals: 
        ans.append(list(val))

    return ans


print(transpose([[1,2,3],[4,5,6]]))