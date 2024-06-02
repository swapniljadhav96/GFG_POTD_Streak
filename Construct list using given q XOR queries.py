'''
Construct list using given q XOR queries
MediumAccuracy: 50.86%Submissions: 24K+Points: 4
In need of more Geekbits? Win from a pool of 3500+ Geekbits via DSA-based Coding Contest every sunday!

banner
Given a list s that initially contains only a single value 0. There will be q queries of the following types:

0 x: Insert x in the list
1 x: For every element a in s, replace it with a ^ x. ('^' denotes the bitwise XOR operator)
Return the sorted list after performing the given q queries.

Example 1:

Input:
q = 5
queries[] = {{0, 6}, {0, 3}, {0, 2}, {1, 4}, {1, 5}}
Output:
1 2 3 7
Explanation:
[0] (initial value)
[0 6] (add 6 to list)
[0 6 3] (add 3 to list)
[0 6 3 2] (add 2 to list)
[4 2 7 6] (XOR each element by 4)
[1 7 2 3] (XOR each element by 5)
The sorted list after performing all the queries is [1 2 3 7]. 
Example 2:
Input:
q = 3
queries[] = {{0, 2}, {1, 3}, {0, 5}} 
Output :
1 3 5
Explanation:
[0] (initial value)
[0 2] (add 2 to list)
[3 1] (XOR each element by 3)
[3 1 5] (add 5 to list)
The sorted list after performing all the queries is [1 3 5].

Your Task:  
You don't need to read input or print anything. Your task is to complete the function constructList() which takes an integer q the number of queries and queries[] a list of lists of length 2 denoting the queries as input parameters and returns the final constructed list.


Expected Time Complexity: O(q*log(q))
Expected Auxiliary Space: O(l), where l is only used for output-specific requirements.


Constraints:
1 ≤ q ≤ 105

'''
from typing import List

class Solution:
    def constructList(self, q: int, queries: List[List[int]]) -> List[int]:
        # Initialize the list with a single element 0
        s = [0]
        # Initialize the cumulative XOR value
        xor_cumulative = 0
        
        # Iterate through each query
        for query in queries:
            if query[0] == 0:
                # Insert x into the list with cumulative XOR applied
                s.append(query[1] ^ xor_cumulative)
            elif query[0] == 1:
                # Update the cumulative XOR with x
                xor_cumulative ^= query[1]
        
        # Apply the final cumulative XOR to all elements in the list
        s = [a ^ xor_cumulative for a in s]
        
        # Sort the list and return it
        s.sort()
        return s
