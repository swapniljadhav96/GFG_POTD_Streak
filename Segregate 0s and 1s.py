'''
Segregate 0s and 1s

Given an array arr consisting of only 0's and 1's in random order. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Examples :

Input: arr[] = [0, 0, 1, 1, 0]
Output: [0, 0, 0, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 1, 1].
Input: arr[] = [1, 1, 1, 1]
Output: [1, 1, 1, 1]
Explanation: There are no 0s in the given array, so the modified array is [1, 1, 1, 1]
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 1
'''


class Solution:
    def segregate0and1(self, arr):
        left = 0
        right = len(arr) - 1

        while left < right:
            # Increment left index while we see 0 at left
            while left < right and arr[left] == 0:
                left += 1

            # Decrement right index while we see 1 at right
            while left < right and arr[right] == 1:
                right -= 1

            # If left is less than right then there is a 1 at left
            # and a 0 at right. Swap arr[left] and arr[right]
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

