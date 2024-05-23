
class Solution:
    def kPalindrome(self, str, n, k):
        # Initialize the DP table
        dp = [[0] * n for _ in range(n)]
        
        # Fill the table for substrings of length 2 and more
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if str[i] == str[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])
        
        # The value dp[0][n-1] gives the minimum number of deletions needed
        # to make the whole string a palindrome
        return 1 if dp[0][n-1] <= k else 0