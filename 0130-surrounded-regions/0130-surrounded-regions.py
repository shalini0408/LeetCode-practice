class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        safe = set()
        rows = len(board)
        cols = len(board[0])
        def dfs(row,col):
            if (row,col) in safe:
                return
            safe.add((row,col))
            directions =[(row,col+1),(row,col-1),(row-1,col),(row+1,col)]
            for (x,y) in directions:
                if 0<= x <rows and 0<= y <cols:
                    if board[x][y] == 'O':
                        dfs(x,y)

        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0,c)
        for c in range(cols):
             if board[rows-1][c]=='O':
                dfs(rows-1,c)
        for r in range(rows):
            if board[r][cols-1] == 'O':
                dfs(r,cols-1)
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'
    
        


        