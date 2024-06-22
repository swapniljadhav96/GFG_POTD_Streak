'''
Extract the Number from the String

Given a sentence containing several words and numbers. Find the largest number among them which does not contain 9. If no such number exists, return -1.

Note: Numbers and words are separated by spaces only. It is guaranteed that there are no leading zeroes in the answer.

Examples :

Input: sentence="This is alpha 5057 and 97"
Output: 5057
Explanation: 5057 is the only number that does not have a 9.
Input: sentence="Another input 9007"
Output: -1
Explanation: Since there is no number that does not contain a 9,output is -1.
Expected Time Complexity: O(n)
Expected Auxillary Space: O(n)

Constraints:
1<=n<=106
1<=answer<=1018

n is the length of a given sentence.
'''

class Solution:
    def ExtractNumber(self, sentence: str) -> int:
        # Split the sentence into words
        words = sentence.split()
        
        # Initialize a variable to keep track of the largest number
        largest_number = -1
        
        # Iterate through the words
        for word in words:
            # Check if the word is a number and does not contain '9'
            if word.isdigit() and '9' not in word:
                # Convert the word to an integer
                number = int(word)
                # Update the largest number if this number is larger
                if number > largest_number:
                    largest_number = number
        
        return largest_number

