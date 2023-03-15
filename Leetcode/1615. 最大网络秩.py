from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # Create an adjacency matrix
        adj = [[0] * n for _ in range(n)]
        for i, j in roads:
            adj[i][j] = 1
            adj[j][i] = 1
        # Count the number of roads for each city
        roads = [sum(row) for row in adj]
        # Find the maximum rank
        max_rank = 0
        for i in range(n):
            for j in range(i + 1, n):
                max_rank = max(max_rank, roads[i] + roads[j] - adj[i][j])
        return max_rank
    
