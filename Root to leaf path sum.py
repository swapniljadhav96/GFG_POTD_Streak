'''
Root to leaf path sum

Given a binary tree and an integer target, check whether there is a root-to-leaf path with its sum as target.

Examples :

Input: tree = 1, target = 2
            /   \
          2     3
Output: false
Explanation: There is no root to leaf path with sum 2.
Input: tree = 1,  target = 4
            /   \
          2     3
Output: true
Explanation: The sum of path from leaf node 3 to root 1 is 4.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(height of tree)

Constraints:
1 ≤ number of nodes ≤ 104
1 ≤ target ≤ 106

'''


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, target):
        if root is None:
            return False

        # Check if we are at a leaf node
        if root.left is None and root.right is None:
            return root.data == target
        
        # Recursively check the left and right subtrees
        remaining_sum = target - root.data
        return (self.hasPathSum(root.left, remaining_sum) or 
                self.hasPathSum(root.right, remaining_sum))

# Example usage:
# Constructing the tree
#       1
#      / \
#     2   3

root = Node(1)
root.left = Node(2)
root.right = Node(3)

solution = Solution()
