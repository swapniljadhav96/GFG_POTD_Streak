'''
Shortest Path in Weighted undirected graph

You are given a weighted undirected graph having n vertices numbered from 1 to n and m edges along with their weights. Find the shortest path between the vertex 1 and the vertex n,  if there exists a path, and return a list of integers whose first element is the weight of the path, and the rest consist of the nodes on that path. If no path exists, then return a list containing a single element -1.

The input list of edges is as follows - {a, b, w}, denoting there is an edge between a and b, and w is the weight of that edge.

Note: The driver code here will first check if the weight of the path returned is equal to the sum of the weights along the nodes on that path, if equal it will output the weight of the path, else -2. In case the list contains only a single element (-1) it will simply output -1. 

Examples :

Input: n = 5, m= 6, edges = [[1, 2, 2], [2, 5, 5], [2, 3, 4], [1, 4, 1], [4, 3, 3], [3, 5, 1]]
Output: 5
Explanation: Shortest path from 1 to n is by the path 1 4 3 5 whose weight is 5. 
Input: n = 2, m= 1, edges = [[1, 2, 2]]
Output: 2
Explanation: Shortest path from 1 to 2 is by the path 1 2 whose weight is 2. 
Input: n = 2, m= 0, edges = [ ]
Output: -1
Explanation: Since there are no edges, so no answer is possible.
Expected Time Complexity: O(m* log(n))
Expected Space Complexity: O(n+m)

Constraint:
2 <= n <= 106
0 <= m <= 106
1 <= a, b <= n
1 <= w <= 105

'''

from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Step 1: Create the graph using adjacency list
        graph = [[] for _ in range(n + 1)]
        for a, b, w in edges:
            graph[a].append((b, w))
            graph[b].append((a, w))
        
        # Step 2: Dijkstra's algorithm
        def dijkstra(source: int, destination: int):
            min_heap = [(0, source)]
            dist = [float('inf')] * (n + 1)
            parent = [-1] * (n + 1)
            dist[source] = 0
            
            while min_heap:
                current_dist, u = heapq.heappop(min_heap)
                
                if u == destination:
                    break
                
                for v, weight in graph[u]:
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
                        heapq.heappush(min_heap, (dist[v], v))
                        parent[v] = u
            
            # If the destination is unreachable, return -1
            if dist[destination] == float('inf'):
                return [-1]
            
            # Step 3: Reconstruct the path from source to destination
            path = []
            node = destination
            while node != -1:
                path.append(node)
                node = parent[node]
            path.reverse()
            
            return [dist[destination]] + path
        
        # Run Dijkstra from 1 to n
        return dijkstra(1, n)

