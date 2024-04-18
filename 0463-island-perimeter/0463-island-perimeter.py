class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    count = self.countIsland(grid, i, j, 0)
                    return count
    
    def countIsland(self, grid: List[List[int]], i: int, j: int, count: int) -> int:
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1:
            return 1
        elif grid[i][j] == 0:
            return 1
        elif grid[i][j] == -1:
            return 0
        else:
            grid[i][j] = -1
            return self.countIsland(grid, i+1, j, 1) + self.countIsland(grid, i-1, j, 1) + self.countIsland(grid, i, j+1, 1) + self.countIsland(grid, i, j-1, 1)