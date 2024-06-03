'''
Trail of ones

Given a number n, find the number of binary strings of length n that contain consecutive 1's in them. Since the number can be very large, return the answer after modulo with 1e9+7.

Example 1:

Input:
n = 2
Output:
1
Explanation:
There are 4 strings of 
length 2, the strings 
are 00, 01, 10, and 
11. Only the string 11 
has consecutive 1's.
Example 2:

Input:
n = 5
Output:
19
Explanation:
There are 19 strings
having consecutive 1's.
Your Task:

You don't need to read input or print anything. Your task is to complete the function numberOfConsecutiveOnes() which takes an integer n and returns the number of binary strings that contain consecutive 1's in them.

Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints
2 <= n <= 105
'''
class Solution:
    def numberOfConsecutiveOnes(self, n):
        MOD = int(1e9+7)
        
        if n == 2:
            return 1
        
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1
        dp[1] = 2
        
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % MOD
        
        total = pow(2, n, MOD)
        
        return (total - dp[n] + MOD) % MOD
