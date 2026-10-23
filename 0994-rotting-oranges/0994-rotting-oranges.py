class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols =len(grid), len(grid[0])
        minutes=0
        fresh=0     
        queue = collections.deque()               
        for r in range(rows):
            for c in range(cols):
                if (grid[r][c]==2):
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh+=1

        while queue and fresh>0:
                length = len(queue)
                for _ in range(length):
                    r,c = queue.popleft()
                    directions = [(1, 0), (-1, 0),(0, 1),(0, -1)]
                    for dr, dc in directions:
                        nr = r + dr
                        nc = c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                            grid[nr][nc] = 2
                            fresh -= 1
                            queue.append((nr, nc))
                minutes += 1
        if fresh > 0:
             return -1
                    
        return minutes
        