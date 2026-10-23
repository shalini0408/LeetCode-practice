class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def dfs(i,j,memo):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m-1 and j == n-1:
                return 1
            directions=[(i+1,j),(i,j+1)]
            paths = 0
            for (row,col) in directions:
                if 0<=row<m and 0<=col<n:
                    paths = paths + dfs(row,col,memo)
                    memo[(i,j)]=paths
            return paths
        return dfs(0,0,memo)
        