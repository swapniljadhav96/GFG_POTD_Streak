'''

Make Binary Tree From Linked List

Given a Linked List Representation of Complete Binary Tree. The task is to construct the Binary tree and print the level order traversal of the Binary tree. 
Note: The complete binary tree is represented as a linked list in a way where if the root node is stored at position i, its left, and right children are stored at position 2*i+1, and 2*i+2 respectively. H is the height of the tree and this space is used implicitly for the recursion stack.

Examples:

Input: n = 5, k = 1->2->3->4->5
Output: 1 2 3 4 5
Explanation: The tree would look like
      1
    /   \
   2     3
 /  \
4   5
Now, the level order traversal of
the above tree is 1 2 3 4 5.
Input: n = 5, k = 5->4->3->2->1
Output: 5 4 3 2 1
Explanation: The tree would look like
     5
   /  \
  4    3
 / \
2   1
Now, the level order traversal of
the above tree is 5 4 3 2 1.
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
Constraints:
1 <= n <= 105
1 <= ki <= 105


'''

# Linked List Node structure
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

# Binary Tree Node structure
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to make binary tree from linked list.
def convert(head):
    if not head:
        return None
    
    # Creating the root of the binary tree
    root = TreeNode(head.data)
    head = head.next
    
    # Queue to keep track of tree nodes
    queue = [root]
    
    while head:
        # Get the current tree node from the queue
        current = queue.pop(0)
        
        # Create the left child from the current linked list node
        leftChild = TreeNode(head.data)
        current.left = leftChild
        queue.append(leftChild)
        head = head.next
        
        # If there's another linked list node, create the right child
        if head:
            rightChild = TreeNode(head.data)
            current.right = rightChild
            queue.append(rightChild)
            head = head.next
    
    return root

# Function to perform level order traversal on the binary tree
def levelOrderTraversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        result.append(current.data)
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    
    return result

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    
    return head
