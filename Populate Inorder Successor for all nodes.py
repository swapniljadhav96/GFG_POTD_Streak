'''
Populate Inorder Successor for all nodes
Difficulty: MediumAccuracy: 51.2%Submissions: 49K+Points: 4
Given a Binary Tree, complete the function to populate the next pointer for all nodes. The next pointer for every node should point to the Inorder successor of the node.
You do not have to return or print anything. Just make changes in the root node given to you.

Note: The node having no in-order successor will be pointed to -1. You don't have to add -1 explicitly, the driver code will take care of this.

Examples :

Input:
       10
       /  \
      8   12
     /
    3
Output: 3->8 8->10 10->12 12->-1
Explanation: The inorder of the above tree is : 3 8 10 12. So the next pointer of node 3 is pointing to 8 , next pointer of 8 is pointing to 10 and so on.And next pointer of 12 is pointing to -1 as there is no inorder successor of 12.
Input:
       1
      /  
     2 
   /
 3  
Output: 3->2 2->1 1->-1
Explanation: The inorder of the above tree is: 3 2 1. So the next pointer of node 3 is pointing to 2 , next pointer of 2 is pointing to 1. And next pointer of 1 is pointing to -1 as there is no inorder successor of 1.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1<= no. of nodes <=105
1<= data of the node <=105

'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
        self.next = None

class Solution:
    def populateNext(self, root):
        # Initialize the previous node as None
        self.prev = None
        
        # Helper function to perform in-order traversal and update next pointers
        def inorder(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder(node.left)
            
            # Visit the current node
            if self.prev:
                self.prev.next = node
            self.prev = node
            
            # Traverse the right subtree
            inorder(node.right)
        
        # Start in-order traversal from the root
        inorder(root)


