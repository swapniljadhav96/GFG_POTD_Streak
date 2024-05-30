'''

String Subsequence

Given two strings, s1 and s2, count the number of subsequences of string s1 equal to string s2.

Return the total count modulo 1e9+7.

Example 1:

Input: s1 = geeksforgeeks, s2 = gks
Output: 4
Explaination: We can pick characters from s1 as a subsequence from indices {0,3,4}, {0,3,12}, {0,11,12} and {8,11,12}.So total 4 subsequences of s1 that are equal to s2.
Example 2:

Input: s1 = problemoftheday, s2 = geek
Output: 0
Explaination: No subsequence of string s1 is equal to string s2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function countWays() which takes the string s1 and s2 as input parameters and returns the number of subsequences of s1 equal to s2.

Expected Time Complexity: O(n*m)  [n and m are lengths of the strings s1 and s2]
Expected Auxiliary Space: O(n*m)     [n and m are lengths of the strings s1 and s2]

Constraints:
1 ≤ n, m ≤ 500  [n and m are lengths of the strings s1 and s2]
'''

class Solution:
    def countWays(self, s1: str, s2: str) -> int:
        MOD = 10**9 + 7
        n = len(s1)
        m = len(s2)
        
        # Create a 2D dp array with dimensions (n+1) x (m+1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Initialize base cases
        for i in range(n + 1):
            dp[i][0] = 1  # There is one way to match an empty subsequence
        
        # Fill the dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    # Two options: either include s1[i-1] or don't
                    dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD
                else:
                    # Only option: don't include s1[i-1]
                    dp[i][j] = dp[i - 1][j] % MOD
        
        # The answer is the number of ways to match the entire s2 from s1
        return dp[n][m]


