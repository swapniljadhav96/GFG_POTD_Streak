'''
Identical Linked Lists

Given the two singly Linked Lists respectively. The task is to check whether two linked lists are identical or not. 
Two Linked Lists are identical when they have the same data and with the same arrangement too. If both Linked Lists are identical then return true otherwise return false. 

Examples:

Input:
LinkedList1: 1->2->3->4->5->6
LinkedList2: 99->59->42->20
Output: false
Explanation:

As shown in figure linkedlists are not identical.
Input:
LinkedList1: 1->2->3->4->5
LinkedList2: 1->2->3->4->5
Output: true
Explanation: 
 
As shown in figure both are identical.
Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
1 <= length of lists <= 103
'''

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Function to check whether two linked lists are identical or not.
def areIdentical(head1, head2):
    # Initialize current pointers for both lists
    current1 = head1
    current2 = head2
    
    # Traverse both lists
    while current1 is not None and current2 is not None:
        # Compare data of both nodes
        if current1.data != current2.data:
            return False
        
        # Move to the next nodes
        current1 = current1.next
        current2 = current2.next
    
    # Check if both lists have ended
    if current1 is None and current2 is None:
        return True
    else:
        return False
