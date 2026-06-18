from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        row = len(grid)
        col = len(grid[0])
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        island = 0

        def get_nei(r, c):
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    yield nr, nc
         
        def dfs(r, c):
            if (r, c) in visited or grid[r][c] == '0':
                return

            visited.add((r, c))
            for nr, nc in get_nei(r, c):
                dfs(nr, nc)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    island += 1

        return island

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
       
#         def dfs(r, c, grid):
#             grid[r][c] = '0'
#             neighbours = get_neighbours(r, c, grid)
#             if not neighbours:
#                 return
           
#             for nr, nc in neighbours:
#                 dfs(nr, nc, grid)
        
#         def get_neighbours(r, c, grid):
#             ROW = len(grid)
#             COL = len(grid[0])
#             neighbours = []
#             directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#             for nr, nc in directions:
#                 new_r = r + nr
#                 new_c = c + nc
#                 if new_r >= 0 and new_r < ROW and new_c >= 0 and new_c < COL and grid[new_r][new_c] == '1':
#                     neighbours.append([new_r, new_c])
#             return neighbours
        
#         islands = 0
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == '1':
                    
#                     dfs(r, c, grid)
#                     islands += 1
                
#         return islands



# my version
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         visited = set()
#         rows = len(grid)
#         cols = len(grid[0])
#         directions = [(1,0), (0,1), (-1, 0), (0,-1)]
#         count = 0

#         def get_nei(r,c):
#             nei = []
#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc
#                 if 0<= nr < rows and 0<= nc < cols:
#                     nei.append((nr,nc))
#             return nei
        
#         def dfs(r,c):
#             if (r,c) in visited or grid[r][c] == "0":
#                 return
#             visited.add((r,c))
#             for nr , nc in get_nei(r,c):
#                 dfs(nr,nc)

#         for r in range(rows):
#             for c in range(cols):
#                 if grid[r][c] == "1" and (r,c) not in visited:
#                     dfs(r,c)
#                     count += 1
                
#         return count




        
        
        

                    


            
            
        