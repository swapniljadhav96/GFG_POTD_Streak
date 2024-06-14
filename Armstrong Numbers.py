'''
Armstrong Numbers

You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371.

Note: Return "Yes" if it is an Armstrong number else return "No".

Examples

Input: n = 153
Output: Yes
Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153. Hence answer is "Yes".
Input: n = 372
Output: No
Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378. Hence answer is "No".
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)

Constraints:
100 ≤ n <1000

'''

class Solution:
    def armstrongNumber(self, n):
        # Extract digits
        d1 = n // 100  # Hundreds place
        d2 = (n // 10) % 10  # Tens place
        d3 = n % 10  # Units place
        
        # Calculate the sum of the cubes of the digits
        sum_of_cubes = d1**3 + d2**3 + d3**3
        
        # Check if the sum of the cubes is equal to the number itself
        if sum_of_cubes == n:
            return "Yes"
        else:
            return "No"

# Example usage:
# sol = Solution()
# print(sol.armstrongNumber(153))  # Output: "Yes"
# print(sol.armstrongNumber(372))  # Output: "No"
