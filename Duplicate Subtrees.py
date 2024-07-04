'''
Duplicate Subtrees

Given a binary tree, your task is to find all duplicate subtrees from the given binary tree.

Duplicate Subtree : Two trees are duplicates if they have the same structure with the same node values.

Note:  Return the root of each tree in the form of a list array & the driver code will print the tree in pre-order tree traversal in lexicographically increasing order.

Examples:

Input : 
 
Output: 2 4   
        4
Explanation: The above tree have two duplicate subtrees.i.e 
  2
 /
4  and 4. Therefore, you need to return the above tree root in the form of a list.  
Input:     5
          / \
         4   6
        / \
       3   4
          / \
         3   6
Output: 
3
6
Explanation: In the above tree, there are two duplicate subtrees.i.e
3 and 6. Therefore, you need to return the above subtrees root in the form of a list. Here, 4 3  is not considered because for a subtree to be equal, it should have the same values as well as structure. If we consider the first subtree on the left, it has  
two children, 3 on the left and 4 3 6   on the right. And for the second subtree it has 3 on the left and 6 on the right.
Since the structures are not same for the subtrees hence they are not equal
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1<= height of binary tree <=103
'''


from collections import defaultdict

class Solution:
    def printAllDups(self, root):
        """
        Prints all nodes with duplicate values in the given binary tree.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of nodes with duplicate values.
        """

        ans = []  # List to store nodes with duplicates
        d = defaultdict(int)  # Dictionary to track value counts

        def traverse(node):
            """
            Recursive helper function to traverse the tree and track values.

            Args:
                node: The current node in the traversal.

            Returns:
                A string representing the current node's path.
            """

            if not node:
                return ""

            # Construct a unique path string for the current node
            path = str(node.data) + traverse(node.left) + traverse(node.right)

            # Increment the count of the current path
            d[path] += 1

            # Check for duplicate paths and add the node to the results
            if d[path] == 2:
                ans.append(node)

            return path

        # Start the traversal from the root
        traverse(root)

        return ans
