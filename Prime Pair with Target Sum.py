'''
Prime Pair with Target Sum

Given a number n, find out if n can be expressed as a+b, where both a and b are prime numbers. If such a pair exists, return the values of a and b, otherwise return [-1,-1] as an array of size 2.
Note: If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, and a < c then  [a, b] is considered as our answer.

Examples

Input: n = 10
Output: 3 7
Explanation: There are two possiblities 3, 7 & 5, 5 are both prime & their sum is 10, but we'll pick 3, 7 as 3 < 5.
Input: n = 3
Output: -1 -1
Explanation: There are no solutions to the number 3.
Expected Time Complexity: O(n*loglog(n))
Expected Auxiliary Space: O(n)

Constraints:
2 <= n <= 106
'''

from typing import List

class Solution:
    def getPrimes(self, n: int) -> List[int]:
        # Edge case
        if n < 4:
            return [-1, -1]
        
        # Step 1: Use Sieve of Eratosthenes to find all primes up to n
        is_prime = [True] * (n + 1)
        is_prime[0], is_prime[1] = False, False  # 0 and 1 are not primes

        for start in range(2, int(n**0.5) + 1):
            if is_prime[start]:
                for multiple in range(start*start, n + 1, start):
                    is_prime[multiple] = False
        
        # Collecting all prime numbers up to n
        primes = [num for num, prime in enumerate(is_prime) if prime]
        
        # Step 2: Find the pair of primes that sum to n
        for a in primes:
            b = n - a
            if b >= a and is_prime[b]:  # Ensure a <= b and b is prime
                return [a, b]
        
        return [-1, -1]

