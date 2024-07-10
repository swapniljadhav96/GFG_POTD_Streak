'''
Largest square formed in a matrix

Given a binary matrix mat of size n * m, find out the maximum length of a side of a square sub-matrix with all 1s.

Examples:

Input: n = 6, m = 5
mat = [[0, 1, 1, 0, 1], 
       [1, 1, 0, 1, 0],
       [0, 1, 1, 1, 0],
       [1, 1, 1, 1, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 0, 0, 0]]
Output: 3
Explanation: 

The maximum length of a side of the square sub-matrix is 3 where every element is 1.
Input: n = 2, m = 2
mat = [[1, 1], 
       [1, 1]]
Output: 2
Explanation: The maximum length of a side of the square sub-matrix is 2. The matrix itself is the maximum sized sub-matrix in this case.
Input: n = 2, m = 2
mat = [[0, 0], 
       [0, 0]]
Output: 0
Explanation: There is no 1 in the matrix.
Expected Time Complexity: O(n*m)
Expected Auxiliary Space: O(n*m)

Constraints:
1 ≤ n, m ≤ 500
0 ≤ mat[i][j] ≤ 1 

'''


from typing import List

class Solution:
    def maxSquare(self, n: int, m: int, mat: List[List[int]]) -> int:
        # Create a DP table with the same dimensions as mat
        dp = [[0] * m for _ in range(n)]
        max_side = 0
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        # If we are on the first row or first column, the largest square is just the cell itself
                        dp[i][j] = 1
                    else:
                        # Update the dp value for mat[i][j]
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # Update the maximum side length found so far
                    max_side = max(max_side, dp[i][j])
        
        return max_side

