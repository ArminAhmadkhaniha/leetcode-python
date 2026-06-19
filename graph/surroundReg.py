class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return

        rows, cols = len(board), len(board[0])
        visited = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def get_neighbors(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    yield nr, nc

        def dfs(r, c):
            if (r, c) in visited or board[r][c] != 'O':
                return

            visited.add((r, c))

            for nr, nc in get_neighbors(r, c):
                dfs(nr, nc)

    
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)

        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

    
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in visited:
                    board[r][c] = 'X'