'''
Minimum Cost To Make Two Strings Identical

Given two strings x and y, and two values costX and costY, the task is to find the minimum cost required to make the given two strings identical. 
You can delete characters from both the strings. The cost of deleting a character from string X is costX and from Y is costY. 
The cost of removing all characters from a string is the same.

Example 1:

Input: x = "abcd", y = "acdb", costX = 10 
       costY = 20.
Output: 30
Explanation: For Making both strings 
identical we have to delete character 
'b' from both the string, hence cost 
will be = 10 + 20 = 30.
Example 2:

Input : x = "ef", y = "gh", costX = 10
        costY = 20.
Output: 60
Explanation: For making both strings 
identical, we have to delete 2-2 
characters from both the strings, hence 
cost will be = 10 + 10 + 20 + 20 = 60.
Your Task:
You don't need to read or print anything. Your task is to complete the function findMinCost() which takes both strings and the costs as input parameters and returns the minimum cost.

Expected Time Complexity: O(|x|*|y|)
Expected Space Complexity: O(|x|*|y|)

Constraints:
1 ≤ |x|, |y| ≤ 1000
1<= costX, costY <= 105

'''

class Solution:
    def findMinCost(self, x, y, costX, costY):
        m = len(x)
        n = len(y)
        
        # Create a 2D dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case: if one string is empty
        for i in range(1, m + 1):
            dp[i][0] = i * costX''
        
        for j in range(1, n + 1):
            dp[0][j] = j * costY
        
        # Fill dp array using the recurrence relations
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if x[i - 1] == y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + costX, dp[i][j - 1] + costY)
        
        return dp[m][n]
