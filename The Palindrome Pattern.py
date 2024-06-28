
'''
The Palindrome Pattern

Given a two-dimensional integer array arr of dimensions n x n, consisting solely of zeros and ones, identify the row or column (using 0-based indexing) where all elements form a palindrome. If multiple palindromes are identified, prioritize the palindromes found in rows over those in columns. Within rows or columns, the palindrome with the smaller index takes precedence. The result should be represented by the index followed by either 'R' or 'C', indicating whether the palindrome was located in a row or column. The output should be space-separated. If no palindrome is found, return the string -1.

Examples:

Input: 
arr[][] =  [[1, 0, 0], 
           [0, 1, 0],
           [1, 1, 0]]
Output: 1 R
Explanation: In the first test case, 0-1-0 is a palindrome 
occuring in a row having index 1.
Input: 
arr[][] =   [[1, 0],
           [1, 0]]
Output: 0 C
Explanation: 1-1 occurs before 0-0 in the 0th column. And there is no palindrome in the two rows.
Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constraints:
1<= arr.size <= 50
0 <= arr[i][j] <= 1
'''

class Solution:
    def pattern(self, arr):
        def is_palindrome(lst):
            return lst == lst[::-1]

        n = len(arr)
        
        # Check for palindromes in rows
        for i in range(n):
            if is_palindrome(arr[i]):
                return "{} R".format(i)
        
        # Check for palindromes in columns
        for j in range(n):
            column = [arr[i][j] for i in range(n)]
            if is_palindrome(column):
                return "{} C".format(j)
        
        # If no palindromes found
        return -1

