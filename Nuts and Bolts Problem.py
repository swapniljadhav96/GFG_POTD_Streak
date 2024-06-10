'''
Nuts and Bolts Problem

Given a set of n nuts & bolts. There is a one-on-one mapping between nuts and bolts. You have to Match nuts and bolts efficiently. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means the nut can only be compared with the bolt and the bolt can only be compared with the nut to see which one is bigger/smaller.
The elements should follow the following order: { !,#,$,%,&,*,?,@,^ }

Note: Make all the required changes directly in the given arrays, output will be handled by the driver code.

Examples

Input: n = 5, nuts[] = {@, %, $, #, ^}, bolts[] = {%, @, #, $ ^}
Output: 
# $ % @ ^
# $ % @ ^
Explanation: As per the order # should come first after that $ then % then @ and ^. 
Input: n = 9, nuts[] = {^, &, %, @, #, *, $, ?, !}, bolts[] = {?, #, @, %, &, *, $ ,^, !}
Output: 
! # $ % & * ? @ ^
! # $ % & * ? @ ^
Explanation: We'll have to match first ! then  # , $,  %,  &,  *,  @,  ^,  ? as per the required ordering.
Expected Time Complexity: O(n(logn))
Expected Auxiliary Space: O(log(n))

Constraints:
1 <= n <= 9
The arrays 'nuts' and 'bolts' can only consist of the following elements: {'@', '#', '$', '%', '^', '&', '?', '*', '!'}.
All the elements of arrays 'nuts' and 'bolts' should be unique.

'''

# User function Template for python3
class Solution:
    def matchPairs(self, n, nuts, bolts):
        # Predefined order
        order = {'!': 0, '#': 1, '$': 2, '%': 3, '&': 4, '*': 5, '?': 6, '@': 7, '^': 8}
        
        # Sort nuts and bolts using the predefined order
        sorted_nuts = sorted(nuts, key=lambda nut: order[nut])
        sorted_bolts = sorted(bolts, key=lambda bolt: order[bolt])
        
        # Make all the required changes directly in the given arrays
        for i in range(n):
            nuts[i] = sorted_nuts[i]
            bolts[i] = sorted_bolts[i]

