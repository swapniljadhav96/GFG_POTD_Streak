'''
Compare two fractions

You are given a string str containing two fractions a/b and c/d, compare them and return the greater. If they are equal, then return "equal".

Note: The string str contains "a/b, c/d"(fractions are separated by comma(,) & space( )). 

Examples

Input: str = "5/6, 11/45"
Output: 5/6
Explanation: 5/6=0.8333 and 11/45=0.2444, So 5/6 is greater fraction.
Input: str = "8/1, 8/1"
Output: equal
Explanation: We can see that both the fractions are same, so we'll return a string "equal".
Input: str = "10/17, 9/10"
Output: 9/10
Explanation: 10/17 = 0.588 & 9/10 = 0.9, so the greater fraction is "9/10".
Expected Time Complexity: O(len|str|)
Expected Auxiliary Space: O(1)

Constraints:
0<=a,c<=103
1<=b,d<=103

'''

class Solution:
    def compareFrac(self, str):
        # Split the string to get the two fractions
        fraction1, fraction2 = str.split(", ")
        
        # Further split to get numerator and denominator for each fraction
        a, b = map(int, fraction1.split("/"))
        c, d = map(int, fraction2.split("/"))
        
        # Calculate the decimal values of the fractions
        value1 = a / b
        value2 = c / d
        
        # Compare the decimal values and return the appropriate result
        if value1 > value2:
            return fraction1
        elif value1 < value2:
            return fraction2
        else:
            return "equal"

