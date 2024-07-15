

Smallest number
Difficulty: MediumAccuracy: 38.74%Submissions: 55K+Points: 4
Given two integers s and d. The task is to find the smallest number such that the sum of its digits is s and the number of digits in the number are d. Return a string that is the smallest possible number. If it is not possible then return -1.

Examples:

Input: s = 9, d = 2
Output: 18 
Explanation: 18 is the smallest number possible with the sum of digits = 9 and total digits = 2.
Input: s = 20, d = 3 
Output: 299 
Explanation: 299 is the smallest number possible with the sum of digits = 20 and total digits = 3.
Expected Time Complexity: O(d)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ s ≤ 100
1 ≤ d ≤ 6

# python code

class Solution:
    def smallestNumber(self, s, d):
        # code here
        n = 1
        
        for i in range(1, d):
            n *= 10
        
        n1 = n * 10
        
        for i in range(n, n1):
            sum_digits = 0
            x = i
            
            while x > 0:
                sum_digits += x % 10
                x //= 10
            
            if sum_digits == s:
                return str(i)
        
        return str(-1)
