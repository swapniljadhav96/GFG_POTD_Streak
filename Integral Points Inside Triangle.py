'''
Integral Points Inside Triangle

Given three non-collinear points whose co-ordinates are p(p1, p2), q(q1, q2) and r(r1, r2) in the X-Y plane. Return the number of integral / lattice points strictly inside the triangle formed by these points.
Note: - A point in the X-Y plane is said to be an integral / lattice point if both its coordinates are integral.

Examples

Input: p = (0,0), q = (0,5), r = (5,0)
Output: 6
Explanation: 

As shown in figure, points (1,1) (1,2) (1,3) (2,1) (2,2) and (3,1) are the integral points inside the triangle. So total 6 are there.
Input: p = (62,-3), q = (5,-45), r = (-19,-23)
Output: 1129
Explanation: There are 1129 integral points in the triangle formed by p, q and r.
Expected Time Complexity: O(Log2109)
Expected Auxillary Space: O(1)

Constraints:
-109 ≤ x-coordinate, y-coordinate ≤ 109

'''

import math

class Solution:
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def boundaryCount(self, p, q):
        if p[0] == q[0]:
            return abs(p[1] - q[1]) - 1
        if p[1] == q[1]:
            return abs(p[0] - q[0]) - 1
        return self.gcd(abs(p[0] - q[0]), abs(p[1] - q[1])) - 1

    def InternalCount(self, p, q, r):
        boundary = self.boundaryCount(p, q) + self.boundaryCount(p, r) + self.boundaryCount(q, r) + 3
        area = abs(p[0] * (q[1] - r[1]) + q[0] * (r[1] - p[1]) + r[0] * (p[1] - q[1]))
        return (area - boundary + 2) // 2
