from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
       
        def dfs(r, c, grid):
            grid[r][c] = '0'
            neighbours = get_neighbours(r, c, grid)
            if not neighbours:
                return
           
            for nr, nc in neighbours:
                dfs(nr, nc, grid)
        
        def get_neighbours(r, c, grid):
            ROW = len(grid)
            COL = len(grid[0])
            neighbours = []
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for nr, nc in directions:
                new_r = r + nr
                new_c = c + nc
                if new_r >= 0 and new_r < ROW and new_c >= 0 and new_c < COL and grid[new_r][new_c] == '1':
                    neighbours.append([new_r, new_c])
            return neighbours
        
        islands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    
                    dfs(r, c, grid)
                    islands += 1
                
        return islands
        
        

                    


            
            
        