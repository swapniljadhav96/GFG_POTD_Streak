'''
linked list of strings forms a palindrome

Given a linked list with string data, check whether the combined string formed is palindrome. If the combined string is palindrome then return true otherwise return false.

Example:

Input:

Output : true
Explanation: As string "abcddcba" is palindrome the function should return true.
Input:

Output : false
Explanation: As string "abcdba" is not palindrome the function should return false.
Expected Time Complexity:  O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 <= Node.data.length<= 103
1<=list.length<=103

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def compute(head):
    # Initialize an empty string to store the concatenated data
    combined_string = ""
    
    # Traverse the linked list to concatenate the string data
    current = head
    while current is not None:
        combined_string += current.data
        current = current.next
    
    # Check if the combined string is a palindrome
    return combined_string == combined_string[::-1]

# Helper function to create a linked list from a list of strings
def create_linked_list(data_list):
    if not data_list:
        return None
    head = Node(data_list[0])
    current = head
    for data in data_list[1:]:
        current.next = Node(data)
        current = current.next
    return head

# Test cases
head1 = create_linked_list(["a", "b", "c", "d", "d", "c", "b", "a"])
print(compute(head1))  # Output: True

head2 = create_linked_list(["a", "b", "c", "d", "b", "a"])
print(compute(head2))  # Output: False
