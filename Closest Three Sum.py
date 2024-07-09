'''
Closest Three Sum

Given an array, arr of integers, and another number target, find three integers in the array such that their sum is closest to the target. Return the sum of the three integers.

Note: If there are multiple solutions, return the maximum one.

Examples :

Input: arr[] = [-7, 9, 8, 3, 1, 1], target = 2
Output: 2
Explanation: There is only one triplet present in the array where elements are -7,8,1 whose sum is 2.
Input: arr[] = [5, 2, 7, 5], target = 13
Output: 14
Explanation: There is one triplet with sum 12 and other with sum 14 in the array. Triplet elements are 5, 2, 5 and 2, 7, 5 respectively. Since abs(13-12) ==abs(13-14) maximum triplet sum will be preferred i.e 14.
Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(1)

Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i] ≤ 105
1 ≤ target ≤ 105

'''

class Solution:
    def threeSumClosest(self, arr, target):
        arr.sort()
        n = len(arr)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            left, right = i + 1, n - 1
            
            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return current_sum
                
                if abs(target - current_sum) < abs(target - closest_sum) or \
                   (abs(target - current_sum) == abs(target - closest_sum) and current_sum > closest_sum):
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum

