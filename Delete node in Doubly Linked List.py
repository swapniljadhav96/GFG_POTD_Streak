'''
Delete node in Doubly Linked List

Given a doubly Linked list and a position. The task is to delete a node from a given position (position starts from 1) in a doubly linked list and return the head of the doubly Linked list.

Examples:

Input: LinkedList = 1 <--> 3 <--> 4, x = 3
Output: 1 3  
Explanation: 
After deleting the node at position 3 (position starts from 1),the linked list will be now as 1 <--> 3.
 
Input: LinkedList = 1 <--> 5 <--> 2 <--> 9, x = 1
Output: 5 2 9
Explanation:

Expected Time Complexity: O(n)
Expected Auxilliary Space: O(1)

Constraints:
2 <= size of the linked list(n) <= 105
1 <= x <= n
1 <= node.data <= 109


'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def delete_node(self, head, x):
        # If linked list is empty
        if not head:
            return None

        # If head needs to be removed
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        
        current = head
        count = 1
        
        # Traverse the list to find the node at position x
        while current and count < x:
            current = current.next
            count += 1
        
        # If the node to be deleted is found
        if current:
            # If current is not the last node
            if current.next:
                current.next.prev = current.prev
            # If current is not the first node
            if current.prev:
                current.prev.next = current.next
        
        return head
