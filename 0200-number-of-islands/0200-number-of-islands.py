class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid), len(grid[0])

        # def dfs(i,j):
        #     if i<0 or i>=rows or j<0 or j>=cols or grid[i][j]!='1':
        #         return
        #     else:
        #         grid[i][j] = 0
        #         dfs(i,j+1)
        #         dfs(i+1,j)
        #         dfs(i,j-1)
        #         dfs(i-1,j)
        def dfs(i,j):
            stack = [(i,j)]
            while stack:
                r,c= stack.pop()
                if(r<0 or r>=rows or c<0 or c>=cols or grid[r][c]!='1'):
                    continue
                grid[r][c] = '0'
                stack.append((r+1,c))
                stack.append((r,c+1))
                stack.append((r-1,c))
                stack.append((r,c-1))
                
        island =0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island+=1
                    dfs(r,c)
        return island
