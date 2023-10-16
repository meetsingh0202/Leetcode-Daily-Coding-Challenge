class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        def findNumberofIslands(grid):
            def traverse(r, c):
                
                if r < 0 or c < 0 or c >= len(grid[0]) or r >= len(grid) or (r, c) in visited or grid[r][c] == 0:
                    return
                
                visited.add((r, c))
                
                for dr, dc in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                    traverse(r + dr, c + dc)
                    
            islands = 0
            visited = set()
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c] == 1 and (r, c) not in visited:
                        islands += 1
                        traverse(r, c)
            return islands
        
        if findNumberofIslands(grid) != 1:
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if findNumberofIslands(grid) != 1:
                        return 1
                    grid[i][j] = 1
        
        return 2