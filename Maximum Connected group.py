'''
Maximum Connected group

You are given a square binary grid. A grid is considered binary if every value in the grid is either 1 or 0. You can change at most one cell in the grid from 0 to 1. You need to find the largest group of connected  1's. Two cells are said to be connected if both are adjacent to each other and both have the same value.

Examples :

Input: grid = [1, 1]
             [0, 1]
Output: 4
Explanation: By changing cell (2,1), we can obtain a connected group of 4 1's
[1, 1]
[1, 1]
Input: grid = [1, 0, 1]
             [1, 0, 1]
             [1, 0, 1]
Output: 7
Explanation: By changing cell (3,2), we can obtain a connected group of 7 1's
[1, 0, 1]
[1, 0, 1]
[1, 1, 1]
Expected Time Complexity: O(n2)
Expected Auxiliary Space: O(n2)

Constraints:
1 <= size of the grid<= 500
0 <= grid[i][j] <= 1
'''


from typing import List, Tuple

class Solution:
    def MaxConnection(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 0:
            return 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def valid(x: int, y: int) -> bool:
            return 0 <= x < n and 0 <= y < n

        def dfs(x: int, y: int, index: int) -> int:
            stack = [(x, y)]
            size = 0
            while stack:
                cx, cy = stack.pop()
                if not valid(cx, cy) or grid[cx][cy] != 1:
                    continue
                grid[cx][cy] = index
                size += 1
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if valid(nx, ny) and grid[nx][ny] == 1:
                        stack.append((nx, ny))
            return size

        group_size = {}
        index = 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, index)
                    group_size[index] = size
                    index += 1

        max_connected = max(group_size.values(), default=0)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_groups = set()
                    potential_size = 1
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if valid(ni, nj) and grid[ni][nj] > 1:
                            group_index = grid[ni][nj]
                            if group_index not in seen_groups:
                                potential_size += group_size[group_index]
                                seen_groups.add(group_index)
                    max_connected = max(max_connected, potential_size)

        return max_connected

