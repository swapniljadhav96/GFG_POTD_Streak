
'''
Remove all occurences of duplicates in a linked list

Given a sorted linked list, delete all nodes that have duplicate numbers (all occurrences), leaving only numbers that appear once in the original list, and return the head of the modified linked list. 

Examples:

Input: Linked List = 23->28->28->35->49->49->53->53
Output: 23 35
Explanation: 

The duplicate numbers are 28, 49 and 53 which are removed from the list.
Input: Linked List = 11->11->11->11->75->75
Output: Empty list
Explanation: 

All the nodes in the linked list have duplicates. Hence the resultant list would be empty.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ size(list) ≤ 105

'''

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def removeAllDuplicates(self, head):
        # Edge case: if the list is empty or has only one element
        if not head or not head.next:
            return head
        
        # Create a dummy node
        dummy = Node(0)
        dummy.next = head
        
        # Initialize prev to dummy and current to head
        prev = dummy
        current = head
        
        while current:
            # Detect duplicates
            if current.next and current.data == current.next.data:
                # Skip all nodes with the same value
                while current.next and current.data == current.next.data:
                    current = current.next
                # Skip the last duplicate node
                current = current.next
                # Link prev to the node after the last duplicate
                prev.next = current
            else:
                # No duplicates, move prev pointer to current
                prev = current
                current = current.next
        
        return dummy.next
