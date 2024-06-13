'''
Padovan Sequence

Given a number n, find the nth number in the Padovan Sequence.

A Padovan Sequence is a sequence which is represented by the following recurrence relation
P(n) = P(n-2) + P(n-3)
P(0) = P(1) = P(2) = 1

Note: Since the output may be too large, compute the answer modulo 10^9+7.

Examples :

Input: n = 3
Output: 2
Explanation: We already know, P1 + P0 = P3 and P1 = 1 and P0 = 1
Input: n = 4
Output: 2
Explanation: We already know, P4  = P2 + P1 and P2 = 1 and P1 = 1
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 <= n <= 106

'''
class Solution:
    def padovanSequence(self, n):
        MOD = 10**9 + 7
        
        if n == 0 or n == 1 or n == 2:
            return 1
        
        # Initialize the first three Padovan numbers
        p0, p1, p2 = 1, 1, 1
        
        # Iteratively compute the nth Padovan number
        for i in range(3, n + 1):
            pn = (p0 + p1) % MOD
            p0, p1, p2 = p1, p2, pn
        
        return p2

