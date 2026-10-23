class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific= set()
        atlantic=set()

        rows= len(heights)
        cols = len(heights[0])

        def dfs(row,col,visited):
            if row >= rows or row < 0 or col < 0 or col >= cols:
                return
            if (row, col) in visited:
                return

            visited.add((row, col))

            directions = [(row, col - 1),(row, col + 1),(row + 1, col),(row - 1, col)]

            for x, y in directions:
                if 0 <= x < rows and 0 <= y < cols:
                    if heights[row][col] <= heights[x][y]:
                        dfs(x, y, visited)
        
        # pacific cells
        for r in range(rows):
            dfs(r,0,pacific)
        for c in range(cols):
            dfs(0,c,pacific)

        #atlantic cells
        for r in range(rows):
            dfs(r, cols - 1,atlantic)
        for c in range(cols):
            dfs(rows - 1, c,atlantic)    
             
        return list(pacific & atlantic)
    