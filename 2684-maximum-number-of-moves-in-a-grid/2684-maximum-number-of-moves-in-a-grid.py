class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        
        @cache
        def traverse(row, col):
            
            if row >= ROWS or col >= COLS:
                return 0
            
            currVal = grid[row][col]
            
            up, down, right = 0, 0, 0
            
            if row + 1 < ROWS and col + 1 < COLS and grid[row + 1][col + 1] > currVal:
                up = 1 + traverse(row + 1, col + 1)
            
            if col + 1 < COLS and grid[row][col + 1] > currVal:
                right = 1 + traverse(row, col + 1)
            
            if row - 1 >= 0 and col + 1 < COLS and grid[row - 1][col + 1] > currVal:
                down = 1 + traverse(row - 1, col + 1)
            
            return max(up, right, down)
        
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        for i in range(ROWS):
            res = max(res, traverse(i, 0))
            
        return res
            