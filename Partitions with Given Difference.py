
from typing import List

class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        MOD = 10**9 + 7
        total_sum = sum(arr)
        
        # Check if (total_sum + d) is even
        if (total_sum + d) % 2 != 0:
            return 0
        
        target_sum = (total_sum + d) // 2
        
        # Create a dp array initialized to 0
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # There's one way to have sum 0: select no elements

        for num in arr:
            # Update the dp array in reverse order
            for j in range(target_sum, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD

        return dp[target_sum]