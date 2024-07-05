
'''
Vertical Width of a Binary Tree

Given a Binary Tree. You need to find and return the vertical width of the tree.

Examples :

Input:
         1
       /    \
      2      3
     / \    /  \
    4   5  6   7
            \   \
             8   9
Output: 6
Explanation: The width of a binary tree is
the number of vertical paths in that tree.



The above tree contains 6 vertical lines.
Input:
     1
    /  \
   2    3
Output: 3
Explanation: The above tree has 3 vertical lines, hence the answer is 3.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(height of the tree).

Constraints:
1 <= number of nodes <= 104


'''


from collections import deque

# Definition for a binary tree node.
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# Function to find the vertical width of a Binary Tree.
def verticalWidth(root):
    if not root:
        return 0

    # Using a dictionary to keep track of horizontal distances.
    hd_set = set()

    # Queue to perform level order traversal. Stores tuples of node and its horizontal distance.
    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()
        
        # Add this horizontal distance to the set.
        hd_set.add(hd)

        # If there's a left child, add it to the queue with hd-1.
        if node.left:
            queue.append((node.left, hd - 1))
        
        # If there's a right child, add it to the queue with hd+1.
        if node.right:
            queue.append((node.right, hd + 1))

    # The number of distinct horizontal distances is the vertical width of the tree.
    return len(hd_set)
