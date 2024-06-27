'''
Toeplitz matrix

A Toeplitz (or diagonal-constant) matrix is a matrix in which each descending diagonal from left to right is constant, i.e., all elements in a diagonal are the same. Given a rectangular matrix mat, your task is to complete the function isToeplitz which returns true if the matrix is Toeplitz otherwise, it returns false.

Examples:

Input:
mat = [[6, 7, 8],
       [4, 6, 7],
       [1, 4, 6]]
Output: true
Explanation: The test case represents a 3x3 matrix
 6 7 8 
 4 6 7 
 1 4 6
Output will be true, as values in all downward diagonals from left to right contain the same elements.
Input: 
mat = [[1,2,3],
       [4,5,6]]
Output: false
Explanation: Matrix of order 2x3 will be 1 2 3 4 5 6 Output: false as values in all diagonals are not the same.
Constraints:
1<=mat.size,mat[0].size<=40
0<=mat[i][j]<=100

Expected time complexity: O(n*m)
Expected space complexity: O(1)

'''


def isToeplitz(mat):
    rows = len(mat)
    cols = len(mat[0])
    
    # Check each element in the first row
    for col in range(cols):
        if not check_diagonal(mat, 0, col):
            return False
    
    # Check each element in the first column
    for row in range(1, rows):  # start from 1 to avoid double checking the (0,0) diagonal
        if not check_diagonal(mat, row, 0):
            return False
    
    return True

def check_diagonal(mat, start_row, start_col):
    rows = len(mat)
    cols = len(mat[0])
    value = mat[start_row][start_col]
    row = start_row
    col = start_col
    
    while row < rows and col < cols:
        if mat[row][col] != value:
            return False
        row += 1
        col += 1
    
    return True
