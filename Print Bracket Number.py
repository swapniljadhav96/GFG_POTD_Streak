'''
Print Bracket Number

Given a string str, the task is to find the bracket numbers, i.e., for each bracket in str, return i if the bracket is the ith opening or closing bracket to appear in the string. 

 Examples:

Input:  str = "(aa(bdc))p(dee)"
Output: 1 2 2 1 3 3
Explanation: The highlighted brackets in
the given string (aa(bdc))p(dee) are
assigned the numbers as: 1 2 2 1 3 3.
Input:  str = "(((()("
Output: 1 2 3 4 4 5
Explanation: The highlighted brackets in
the given string (((()( are assigned
the numbers as: 1 2 3 4 4 5
Expected Time Complexity: O(|str|)
Expected Auxiliary Space: O(|str|)

Constraints:
1 <= |str| <= 105
str contains lowercase English alphabets, and '(', ')' characters
At any index, the number of opening brackets is greater than or equal to closing brackets

'''

class Solution:
    def bracketNumbers(self, str):
        # Stack to keep track of the positions of opening brackets
        stack = []
        # List to store the result
        result = []
        # Counter to assign bracket numbers
        counter = 1
        
        for char in str:
            if char == '(':
                # Push the current counter to the stack
                stack.append(counter)
                # Append the counter to the result list
                result.append(counter)
                # Increment the counter for the next bracket
                counter += 1
            elif char == ')':
                # Pop the most recent opening bracket number from the stack
                if stack:
                    result.append(stack.pop())
        
        return result

